from typing import Optional, List
from dataclasses import dataclass

from sqlalchemy import text

from database.connection import get_session

@dataclass
class Disciplina:

    id_disciplina: Optional[int] = None
    nome: str
    carga_horaria: int
    semestre: str

class DisciplinaRepository:

    def buscarDisciplinaPorId(self, id_disciplina: int) -> Optional[Disciplina]:

        session = get_session()

        try:
            resultado = session.execute(text("""
                    SELECT
                        id_disciplina,
                        nome,
                        carga_horaria,
                        semestre
                    FROM disciplinas
                    WHERE id_disciplina = :id
                """),{"id": id_disciplina})

            linha = resultado.mappings().first()

            return Disciplina(**linha) if linha else None
        finally:
            session.close()


    def buscarDisciplina(self, nome: str, carga_horaria: int, semestre: str) -> Optional[Disciplina]:

        session = get_session()

        try:
            resultado = session.execute(text("""
                    SELECT
                        id_disciplina,
                        nome,
                        carga_horaria,
                        semestre
                    FROM disciplinas
                    WHERE nome = :nome
                      AND carga_horaria = :carga_horaria
                      AND semestre = :semestre
                """),{"nome": nome, "carga_horaria": carga_horaria, "semestre": semestre})

            linha = resultado.mappings().first()

            return Disciplina(**linha) if linha else None
        finally:
            session.close()


    def listar(self) -> List[Disciplina]:

        session = get_session()

        try:
            resultado = session.execute(text("""
                    SELECT
                        id_disciplina,
                        nome,
                        carga_horaria,
                        semestre
                    FROM disciplinas
                    ORDER BY nome
                """))

            linhas = resultado.mappings().all()

            return [Disciplina(**linha) for linha in linhas]
        finally:
            session.close()


    def inserir(self, disciplina: Disciplina) -> None:

        session = get_session()

        try:
            session.execute(text("""
                    INSERT INTO disciplinas
                        (nome, carga_horaria, semestre)
                    VALUES
                        (:nome, :carga_horaria, :semestre)
                """),{"nome": disciplina.nome, "carga_horaria": disciplina.carga_horaria,"semestre": disciplina.semestre})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


    def deletar(self, id_disciplina: int) -> None:

        session = get_session()

        try:
            session.execute(text("""
                    DELETE
                    FROM disciplinas
                    WHERE id_disciplina = :id
                """), {"id": id_disciplina})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()