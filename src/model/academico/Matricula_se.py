from typing import List, Optional
from dataclasses import dataclass

from sqlalchemy import text

from database.connection import get_session

@dataclass
class Matricula_se:

    aluno_id: Optional[int] = None
    disciplina_id: Optional[int] = None
    turma_id: Optional[int] = None

class MatriculaSeRepository:

    def buscar(self, id_aluno: int, id_disciplina: int, id_turma: int)-> Optional[MatriculaSe]:

    session = get_session()

    try:
        resultado = session.execute(text("""SELECT id_aluno,
                    id_disciplina,
                    id_turma
                FROM matricula_se
                WHERE id_aluno = :id_aluno
                  AND id_disciplina = :id_disciplina
                  AND id_turma = :id_turma
            """), {"id_aluno": id_aluno,"id_disciplina": id_disciplina, "id_turma": id_turma
            })

        linha = resultado.mappings().first()

        return MatriculaSe(**linha) if linha else None

    finally:
        session.close()

    def listar(self) -> List[MatriculaSe]:
        session = get_session()

        try:
            resultado = session.execute(text("""
                    SELECT
                        id_aluno,
                        id_disciplina,
                        id_turma
                    FROM matricula_se
                    ORDER BY id_aluno
                """))

            linhas = resultado.mappings().all()

            return [MatriculaSe(**linha) for linha in linhas]

        finally:
            session.close()

    def inserir(self, matricula: MatriculaSe) -> None:

        session = get_session()

        try:
            session.execute(text("""
                    INSERT INTO matricula_se
                        (id_aluno, id_disciplina, id_turma)
                    VALUES
                        (:id_aluno, :id_disciplina, :id_turma)
                """),{"id_aluno": matricula.id_aluno,"id_disciplina": matricula.id_disciplina,"id_turma": matricula.id_turma})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_aluno: int, id_disciplina: int, id_turma: int) -> None:

        session = get_session()

        try:
            session.execute(text("""
                    DELETE
                    FROM matricula_se
                    WHERE id_aluno = :id_aluno
                      AND id_disciplina = :id_disciplina
                      AND id_turma = :id_turma
                """),{"id_aluno": id_aluno,"id_disciplina": id_disciplina, "id_turma": id_turma})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()