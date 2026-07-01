from typing import Optional, List
from dataclasses import dataclass
from datetime import time
from enum import Enum

from sqlalchemy import text
from database.connection import get_session


class Presenca(Enum):
    PRESENTE = 'P'
    FALTA = 'F'

@dataclass
class Frequencia:

    id_frequencia: Optional[int] = None
    hora_saida: time
    hora_entrada: time
    presente: Presenca

class FrequenciaRepository:

    def buscarPorId(self, id_frequencia: int) -> Optional[Frequencia]:

        session = get_session()
        
        try:
            resultado = session.execute(text("SELECT id_frequencia, hora_saida, hora_entrada, presente FROM frequencia WHERE id_frequencia = :id_frequencia"), {"id_frequencia": id_frequencia})
            
            linha = resultado.mappings().first()
            
            return Frequencia(**linha) if linha else None

        finally:
            session.close()

    def listar(self) -> List[Frequencia]:

        session = get_session()
        
        try:
            resultado = session.execute(text("SELECT id_frequencia, hora_saida, hora_entrada, presente FROM frequencia ORDER BY id_frequencia"))
            
            linhas = resultado.mappings().all()
            
            return [Frequencia(**linha) for linha in linhas]

        finally:
            session.close()

    def inserir(self, frequencia: Frequencia) -> int:
       
        session = get_session()
        
        try:

            if self.buscarPorId(frequencia.id_frequencia) is not None:
                raise ValueError("Frequência já existe.")
                
            resultado = session.execute(
                text("INSERT INTO frequencia (hora_saida, hora_entrada, presente) VALUES (:hora_saida, :hora_entrada, :presente) RETURNING id_frequencia"),
                {"hora_saida": frequencia.hora_saida, "hora_entrada": frequencia.hora_entrada, "presente": frequencia.presente.value}
            )
            
            novo_id = resultado.scalar()
            session.commit()
          
            return novo_id

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_frequencia: int) -> None:

        session = get_session()
       
        try:
            session.execute(text("DELETE FROM frequencia WHERE id_frequencia = :id_frequencia"), {"id_frequencia": id_frequencia})
            
            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()