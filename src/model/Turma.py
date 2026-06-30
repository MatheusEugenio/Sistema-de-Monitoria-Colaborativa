from typing import Optional, List
from dataclasses import dataclass
from datetime import time
import psycopg2.extras
from database.connection import get_connection

@dataclass
class Turma:

    id_turma: Optional[int] = None
    semestre: str
    codigo: str
    horario: time

class TurmaRepository:

    def listar(self) -> List[Turma]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT id_turma, semestre, codigo, horario FROM turma")

            linhas = cursor.fetchall()

            cursor.close()

            return [
                Turma(
                    id_turma=l["id_turma"],
                    semestre=l["semestre"],
                    codigo=l["codigo"],
                    horario=l["horario"]
                ) for l in linhas
            ]

        finally:
            connect.close()

    def inserir(self, turma: Turma) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute(
                    """INSERT INTO turma (semestre, codigo, horario) 
                       VALUES (%s, %s, %s)""",
                    (turma.semestre, turma.codigo, turma.horario),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_turma: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute("DELETE FROM turma WHERE id_turma = %s", (id_turma,))

                connect.commit()
                
            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()
                
        finally:
            connect.close()