from typing import Optional, List
from dataclasses import dataclass
import psycopg2.extras
from database.connectection import get_connectection

@dataclass
class Professor:

    id_professor: Optional[int] = None
    departamento: str

class ProfessorRepository:

    def listar(self) -> List[Professor]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT id_professor, departamento FROM professor")

            linhas = cursor.fetchall()

            cursor.close()

            return [
                Professor(
                    id_professor=l["id_professor"],
                    departamento=l["departamento"]
                ) for l in linhas
            ]

        finally:
            connect.close()

    def inserir(self, professor: Professor) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute(
                    "INSERT INTO professor (departamento) VALUES (%s)",
                    (professor.departamento,),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_professor: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute("DELETE FROM professor WHERE id_professor = %s", (id_professor,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()
    
    