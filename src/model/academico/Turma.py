from typing import Optional, List
from dataclasses import dataclass
from datetime import time

from sqlalchemy import text
from database.connection import get_session

@dataclass
class Turma:

    id_turma: Optional[int] = None
    semestre: str
    codigo: str
    horario: time

class TurmaRepository:

    def buscarPorIdTurma(self, id_turma: int) -> Optional[Turma]:

        session = get_session()

        try:

            resultado = session.execute(
                text("""
                    SELECT
                        id_turma,
                        semestre,
                        codigo,
                        horario
                    FROM turma
                    WHERE id_turma = :id
                """),{"id": id_turma})

            linha = resultado.mappings().first()

            return Turma(**linha) if linha else None

        finally:
            session.close()


    def buscarTurma(
        self,
        semestre: str,
        codigo: str
    ) -> Optional[Turma]:

        session = get_session()

        try:

            resultado = session.execute(
                text("""
                    SELECT
                        id_turma,
                        semestre,
                        codigo,
                        horario
                    FROM turma
                    WHERE semestre = :semestre
                      AND codigo = :codigo
                """),{"semestre": semestre,"codigo": codigo})

            linha = resultado.mappings().first()

            return Turma(**linha) if linha else None

        finally:
            session.close()


    def listar(self) -> List[Turma]:

        session = get_session()

        try:

            resultado = session.execute(
                text("""
                    SELECT
                        id_turma,
                        semestre,
                        codigo,
                        horario
                    FROM turma
                    ORDER BY codigo
                """))

            linhas = resultado.mappings().all()

            return [Turma(**linha) for linha in linhas]

        finally:
            session.close()


    def inserir(self, turma: Turma) -> None:

        session = get_session()

        try:
            session.execute(
                text("""
                    INSERT INTO turma
                        (semestre, codigo, horario)
                    VALUES
                        (:semestre, :codigo, :horario)
                """),{"semestre": turma.semestre,"codigo": turma.codigo,"horario": turma.horario})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


    def deletar(self, id_turma: int) -> None:

        session = get_session()

        try:
            session.execute(text("""
                    DELETE
                    FROM turma
                    WHERE id_turma = :id
                """),{"id": id_turma})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()