from typing import Optional, List
from dataclasses import dataclass
from datetime import time, date
from enum import IntEnum
import psycopg2.extras
from database.connectection import get_connection

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
    dia_semana: DiaSemana.SEGUNDA

class DisponibilidadeRepository:

    def buscarDisponibilidadePorId(self, id_disponibilidade: int) -> Optional[Disponibilidade]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("""
                SELECT id_disponibilidade, horario_inicio, horario_fim, 
                       data_inicio, data_fim, dia_semana 
                FROM disponibilidade
                WHERE id_disponibilidade = %s
            """, (id_disponibilidade,))

            linha = cursor.fetchone()

            cursor.close()

            if linha:
                return Disponibilidade(
                    id_disponibilidade=linha["id_disponibilidade"],
                    horario_inicio=linha["horario_inicio"],
                    horario_fim=linha["horario_fim"],
                    data_inicio=linha["data_inicio"],
                    data_fim=linha["data_fim"],
                    dia_semana=DiaSemana(linha["dia_semana"])
                )
            return None
            
        finally:
            connect.close()
            
    def buscarPorData_hora(self, horario_inicio: time, horario_fim: time, data_inicio: date, data_fim: date) -> List[Disponibilidade]:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("""
                SELECT id_disponibilidade, horario_inicio, horario_fim, 
                       data_inicio, data_fim, dia_semana 
                FROM disponibilidade
                WHERE data_inicio <= CURRENT_DATE AND data_fim >= CURRENT_DATE
                      AND horario_inicio <= CURRENT_TIME AND horario_fim >= CURRENT_TIME
            """)

            linhas = cursor.fetchall()

            cursor.close()

            return [
                Disponibilidade(
                    id_disponibilidade=l["id_disponibilidade"],
                    horario_inicio=l["horario_inicio"],
                    horario_fim=l["horario_fim"],
                    data_inicio=l["data_inicio"],
                    data_fim=l["data_fim"],
                    dia_semana=DiaSemana(l["dia_semana"])
                ) for l in linhas
            ]
            
        finally:
            connect.close()

    def listar(self) -> List[Disponibilidade]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("""
                SELECT id_disponibilidade, horario_inicio, horario_fim, 
                       data_inicio, data_fim, dia_semana 
                FROM disponibilidade
            """)

            linhas = cursor.fetchall()

            cursor.close()

            return [
                Disponibilidade(
                    id_disponibilidade=l["id_disponibilidade"],
                    horario_inicio=l["horario_inicio"],
                    horario_fim=l["horario_fim"],
                    data_inicio=l["data_inicio"],
                    data_fim=l["data_fim"],
                    dia_semana=DiaSemana(l["dia_semana"])
                ) for l in linhas
            ]
            
        finally:
            connect.close()

    def inserir(self, disp: Disponibilidade) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()
            
            try:
                cursor.execute(
                    """INSERT INTO disponibilidade (horario_inicio, horario_fim, data_inicio, data_fim, dia_semana) 
                       VALUES (%s, %s, %s, %s, %s)""",
                    (disp.horario_inicio, disp.horario_fim, disp.data_inicio, 
                     disp.data_fim, disp.dia_semana.value),
                )
                
                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_disponibilidade: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute("DELETE FROM disponibilidade WHERE id_disponibilidade = %s", (id_disponibilidade,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()