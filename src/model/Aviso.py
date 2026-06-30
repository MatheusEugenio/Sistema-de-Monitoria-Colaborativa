from typing import Optional, List
from dataclasses import dataclass
from datetime import date
import psycopg2.extras
from database.connectection import get_connection

@dataclass
class Aviso:

    id_aviso: Optional[int] = None
    titulo: str
    descricao: str
    data_publicacao: date

class AvisoRepository:

    def listar(self) -> List[Aviso]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT id_aviso, titulo, descricao, data_publicacao FROM aviso ORDER BY data_publicacao DESC")

            linhas = cursor.fetchall()

            cursor.close()

            return [
                Aviso(
                    id_aviso=l["id_aviso"],
                    titulo=l["titulo"],
                    descricao=l["descricao"],
                    data_publicacao=l["data_publicacao"]
                ) for l in linhas
            ]

        finally:
            connect.close()

    def inserir(self, aviso: Aviso) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    """INSERT INTO aviso (titulo, descricao, data_publicacao) 
                       VALUES (%s, %s, %s)""",
                    (aviso.titulo, aviso.descricao, aviso.data_publicacao),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()
                
        finally:
            connect.close()

    def deletar(self, id_aviso: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()
            try:
                cursor.execute("DELETE FROM aviso WHERE id_aviso = %s", (id_aviso,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()

        finally:
            connect.close()