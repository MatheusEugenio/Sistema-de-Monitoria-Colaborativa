from dataclasses import dataclass
from typing import List, Optional

from sqlalchemy import text
from database.connection import get_session

@dataclass
class Ministra:

    professor_id: int
    disciplina_id:int


class MinistraRepository:

    def jaExiste(self, professor_id: int, disciplina_id: int) -> bool:
        session = get_session()

        try:
            result = session.execute(
                text("SELECT COUNT(*) FROM ministra WHERE professor_id = :professor_id AND disciplina_id = :disciplina_id"),
                {"professor_id": professor_id, "disciplina_id": disciplina_id}
            )
            
            count = result.fetchone()[0]
            return count > 0

        finally:
            session.close()

    def listar(self) -> List[Ministra]:

        session = get_session()

        try:
            result = session.execute(text("SELECT * FROM ministra ORDER BY professor_id"))
            linhas = result.mappings().all()

            return [Ministra(**linha) for linha in linhas]
        finally:
            session.close()

    def inserir(self, ministra: Ministra) -> None:
        
        session = get_session()

        try:
            session.execute(
                text("INSERT INTO ministra (professor_id, disciplina_id) VALUES (:professor_id, :disciplina_id)"),
                {"professor_id": ministra.professor_id, "disciplina_id": ministra.disciplina_id}
            )
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
 
    def deletar(self, professor_id: int, disciplina_id: int) -> None:
        
        session = get_session()
        
        try:

            session.execute(          
            text("""
                DELETE
                FROM ministra
                WHERE professor_id = :professor_id
                  AND disciplina_id = :disciplina_id
            """),{"professor_id": professor_id,"disciplina_id": disciplina_id})

            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
 