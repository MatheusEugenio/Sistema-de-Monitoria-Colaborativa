from typing import Optional, List
from dataclasses import dataclass
from datetime import date, time
import psycopg2.extras
from database.connection import get_connection

@dataclass
class ValidacaoProfessorMonitor:

    id_validacao: Optional[int] = None
    data_validacao: date
    total_horas: time
    status: str
  
class ValidacaoProfessorMonitorRepository:

    def listar(self) -> List[ValidacaoProfessorMonitor]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("""
                SELECT id_validacao, data_validacao, total_horas, status 
                FROM validacao_professor_monitor
            """)

            linhas = cursor.fetchall()

            cursor.close()

            return [
                ValidacaoProfessorMonitor(
                    id_validacao=l["id_validacao"],
                    data_validacao=l["data_validacao"],
                    total_horas=l["total_horas"],
                    status=l["status"]
                ) for l in linhas
            ]

        finally:
            connect.close()

    def inserir(self, validacao: ValidacaoProfessorMonitor) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute(
                    """INSERT INTO validacao_professor_monitor (data_validacao, total_horas, status) 
                       VALUES (%s, %s, %s)""",
                    (validacao.data_validacao, validacao.total_horas, validacao.status),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise
                
            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_validacao: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute("DELETE FROM validacao_professor_monitor WHERE id_validacao = %s", (id_validacao,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()
    