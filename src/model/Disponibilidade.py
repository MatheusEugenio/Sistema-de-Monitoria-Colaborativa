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