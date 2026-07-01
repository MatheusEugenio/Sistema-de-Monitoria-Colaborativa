from typing import Optional, List
from dataclasses import dataclass
from datetime import time
from enum import Enum

import psycopg2.extras
from database.connection import get_connection


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

    def listarFrequencias(self) -> List[Frequencia]:

        connect = get_connection()
        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM frequencia ORDER BY id_frequencia")
            
            linhas = cursor.fetchall()
            
            cursor.close()

            frequencias = []

            for linha in linhas:
                frequencias.append(Frequencia(**linha))

            return frequencias
        finally:
            connect.close()


    def inserir(self, frequencia: Frequencia) -> int:

        connect = get_connection()

        try:    
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            try:
                cursor.execute(
                    "INSERT INTO frequencia (hora_saida, hora_entrada, presente) VALUES (%s, %s, %s) RETURNING id_frequencia",
                    (frequencia.hora_saida, frequencia.hora_entrada, frequencia.presente.value),
                )

                novo_id = cursor.fetchone()["id_frequencia"]
                connect.commit()

                return novo_id
            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_frequencia: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            try:
                cursor.execute("DELETE FROM frequencia WHERE id_frequencia = %s", (id_frequencia,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()


