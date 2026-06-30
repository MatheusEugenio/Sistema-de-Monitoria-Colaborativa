from dataclasses import dataclass
from typing import List, Optional

import psycopg2.extras
from database.connectection import get_connectection

@dataclass
class Ministra:

    professor_id: Optional[int] = None
    disciplina_id: Optional[int] = None


class MinistraRepository:

    def listar(self) -> List[Ministra]:

        connect = get_connectection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictcursor)
        
            cursor.execute("SELECT * FROM ministra ORDER BY professor_id")
            linhas = cursor.fetchall()
            cursor.close()
        
            ministras = []

            for linha in linhas:
                ministras.append(Ministra(**linha))

            return ministras
        finally:
            connect.close()
 
    def inserir(self, ministra: Ministra) -> None:
        
        connect = get_connectection()
        
        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    "INSERT INTO ministra (professor_id, disciplina_id) VALUES (%s, %s)",
                    (ministra.professor_id, ministra.disciplina_id),
                )
                connect.commit()
            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()
 
    def deletar(self, professor_id: int, disciplina_id: int) -> None:
        
        connect = get_connectection()
        
        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    "DELETE FROM ministra WHERE professor_id = %s AND disciplina_id = %s",
                    (professor_id, disciplina_id),
                )
                connect.commit()
            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()
 