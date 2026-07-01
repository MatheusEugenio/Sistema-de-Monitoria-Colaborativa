from typing import List, Optional
from dataclasses import dataclass

from sqlalchemy import text
from database.connectection import get_session

@dataclass
class Material:
    id_material: Optional[int] = None
    tipo_arquivo: str
    link_arquivo: Optional[str] = None
    descricao: str
    titulo: str

class MaterialRepository:

    def buscarPorId(self, id_material: int) -> Optional[Material]:

        session = get_session()

        try:

            resultado = session.execute(

                text("""
                    SELECT
                        id_material,
                        tipo_arquivo,
                        link_arquivo,
                        descricao,
                        titulo
                    FROM material
                    WHERE id_material = :id
                """),

                {"id": id_material}

            )

            linha = resultado.mappings().first()

            return Material(**linha) if linha else None

        finally:

            session.close()


    def buscarArquivo(
        self,
        titulo: str,
        tipo_arquivo: str,
        link_arquivo: Optional[str],
        descricao: str
    ) -> Optional[Material]:

        session = get_session()

        try:

            resultado = session.execute(
                text("""
                    SELECT
                        id_material,
                        tipo_arquivo,
                        link_arquivo,
                        descricao,
                        titulo
                    FROM material
                    WHERE titulo = :titulo
                      AND tipo_arquivo = :tipo_arquivo
                      AND link_arquivo = :link_arquivo
                      AND descricao = :descricao
                """), {"titulo": titulo,
                    "tipo_arquivo": tipo_arquivo,"link_arquivo": link_arquivo,"descricao": descricao})

            linha = resultado.mappings().first()

            return Material(**linha) if linha else None

        finally:
            session.close()


    def listar(self) -> List[Material]:

        session = get_session()

        try:

            resultado = session.execute(
                text("""
                    SELECT
                        id_material,
                        tipo_arquivo,
                        link_arquivo,
                        descricao,
                        titulo
                    FROM material
                    ORDER BY id_material
                """))

            linhas = resultado.mappings().all()

            return [Material(**linha) for linha in linhas]

        finally:
            session.close()


    def inserir(self, material: Material) -> None:

        session = get_session()

        try:

            session.execute(
                text("""
                    INSERT INTO material
                        (tipo_arquivo, link_arquivo, descricao, titulo)
                    VALUES
                        (:tipo_arquivo, :link_arquivo, :descricao, :titulo)
                """), {"tipo_arquivo": material.tipo_arquivo,"link_arquivo": material.link_arquivo,"descricao": material.descricao,"titulo": material.titulo})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


    def deletar(self, id_material: int) -> None:

        session = get_session()

        try:
            session.execute(
                text("""
                    DELETE
                    FROM material
                    WHERE id_material = :id
                """),{"id": id_material})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()