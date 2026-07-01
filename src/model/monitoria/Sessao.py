from typing import Optional, List
from dataclasses import dataclass
from datetime import time
import psycopg2.extras
from database.connection import get_connection

@dataclass
class Sessao:

    id_sessao: Optional[int] = None
    limite_participantes: int
    horario: time
    descricao: str

class SessaoRepository:

    def buscarPorIdSessao(self, id_sessao: int) -> Optional[Sessao]:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT * FROM sessao WHERE id_sessao = %s", (id_sessao,))

            linha = cursor.fetchone()

            return Sessao(**linha) if linha else None

        finally:
            cursor.close()
            connect.close()
            
    def buscarSessao(self, id_sessao: int, horario: time) -> Optional[Sessao]:
        
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT id_sessao, limite_participantes, horario, descricao FROM sessao WHERE id_sessao = %s AND horario = %s", (id_sessao, horario))

            linha = cursor.fetchone()

            cursor.close()

            return Sessao(**linha) if linha else None

        finally:
            connect.close()

    def inserir(self, sessao: Sessao) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            if self.buscarSessao(sessao.id_sessao, sessao.horario):
                raise ValueError(f"Sessão com ID {sessao.id_sessao} e horário {sessao.horario} já existe.")
                
            try:
                cursor.execute(
                    """INSERT INTO sessao (limite_participantes, horario, descricao) 
                       VALUES (%s, %s, %s)""",
                    (sessao.limite_participantes, sessao.horario, sessao.descricao),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_sessao: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute("DELETE FROM sessao WHERE id_sessao = %s", (id_sessao,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()
