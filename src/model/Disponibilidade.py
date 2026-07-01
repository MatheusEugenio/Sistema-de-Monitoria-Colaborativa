from typing import Optional, List
from dataclasses import dataclass
from datetime import time, date
from enum import IntEnum

from sqlalchemy import text
from database.connection import get_session

class DiaSemana(IntEnum):
    SEGUNDA = 0
    TERCA = 1
    QUARTA = 2
    QUINTA = 3
    SEXTA = 4
    SABADO = 5
    DOMINGO = 6


@dataclass
class Disponibilidade:

    id_disponibilidade: Optional[int] = None
    horario_inicio: time
    horario_fim: time
    data_inicio: date
    data_fim: date
    dia_semana: DiaSemana

class DisponibilidadeRepository:

    # para evitar repeticao de retorno do objeto disponibilidade
    def _map(self, l):
        return Disponibilidade(
            id_disponibilidade=l["id_disponibilidade"],
            horario_inicio=l["horario_inicio"],
            horario_fim=l["horario_fim"],
            data_inicio=l["data_inicio"],
            data_fim=l["data_fim"],
            dia_semana=DiaSemana(l["dia_semana"])
        )

    def buscarDisponibilidadePorId(self, id_disponibilidade: int) -> Optional[Disponibilidade]:
        
        session = get_session()
        
        try:
            
            resultado = session.execute(text("SELECT id_disponibilidade, horario_inicio, horario_fim, data_inicio, data_fim, dia_semana FROM disponibilidade WHERE id_disponibilidade = :id_disponibilidade"), {"id_disponibilidade": id_disponibilidade})
           
            linha = resultado.mappings().first()
            
           return [self._map(l) for l in linhas]
        finally:
            session.close()

    def buscarPorData_hora(self,horario_inicio: time, horario_fim: time, data_inicio: date, data_fim: date) -> List[Disponibilidade]:
        
        session = get_session()
        
        try:
            resultado = session.execute(text("SELECT id_disponibilidade, horario_inicio, horario_fim, data_inicio, data_fim, dia_semana FROM disponibilidade"))

            linhas = resultado.mappings().all()
            
           return [self._map(l) for l in linhas]
        finally:
            session.close()

    def listar(self) -> List[Disponibilidade]:
        session = get_session()

        try:
            resultado = session.execute(text("SELECT id_disponibilidade, horario_inicio, horario_fim, data_inicio, data_fim, dia_semana FROM disponibilidade"))
            
            linhas = resultado.mappings().all()

            return [self._map(l) for l in linhas]
        finally:
            session.close()

    def inserir(self, disp: Disponibilidade) -> None:
        
        session = get_session()
        
        try:
            
            session.execute(text("INSERT INTO disponibilidade (horario_inicio, horario_fim, data_inicio, data_fim, dia_semana) VALUES (:horario_inicio, :horario_fim, :data_inicio, :data_fim, :dia_semana)"), {"horario_inicio": disp.horario_inicio, "horario_fim": disp.horario_fim, "data_inicio": disp.data_inicio, "data_fim": disp.data_fim, "dia_semana": disp.dia_semana.value})
            
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_disponibilidade: int) -> None:
        
        session = get_session()
        
        try:
            
            session.execute(text("DELETE FROM disponibilidade WHERE id_disponibilidade = :id_disponibilidade"), {"id_disponibilidade": id_disponibilidade})
            
            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()