from typing import Optional, List
from dataclasses import dataclass

from sqlalchemy import text
from database.connection import get_session

@dataclass
class Professor:

    id_professor: Optional[int] = None
    departamento: str
    usuario_id: Optional[int] = None

class ProfessorRepository:

    def buscarPorIdProfessor(self, id_professor: int) -> Optional[Professor]:

        session = get_session()

        try:

            resultado = session.execute(
                text("SELECT id_professor, departamento, id_usuario FROM professor WHERE id_professor = :id"),
                {"id": id_professor}
            )

            linha = resultado.mappings().first()

            return Professor(**linha) if linha else None

        finally:
            session.close()


    def listar(self) -> List[Professor]:

        session = get_session()

        try:

            resultado = session.execute(text("SELECT id_professor, departamento, id_usuario FROM professor ORDER BY id_professor"))

            linhas = resultado.mappings().all()

            return [Professor(**linha) for linha in linhas]

        finally:
            session.close()


    def inserir(self, professor: Professor) -> None:

        session = get_session()

        try:

            if professor.id_professor is not None and self.buscarPorIdProfessor(professor.id_professor):
                raise ValueError("Professor já cadastrado.")

            session.execute(text("INSERT INTO professor (departamento, id_usuario) VALUES (:departamento, :id_usuario)"),{"departamento": professor.departamento,"id_usuario": professor.id_usuario})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


    def deletar(self, id_professor: int) -> None:

        session = get_session()

        try:
            session.execute(
                text("DELETE FROM professor WHERE id_professor = :id"),
                {"id": id_professor}
            )

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()