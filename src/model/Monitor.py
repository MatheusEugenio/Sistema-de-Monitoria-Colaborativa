from typing import Optional, List
from dataclasses import dataclass
import psycopg2.extras
from database.connectection import get_connectection

@dataclass
class Monitor:

    id_monitor: Optional[int] = None
    departamento: str

class MonitorRepository:

    def listar(self) -> List[Monitor]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT id_monitor, departamento FROM monitor")

            linhas = cursor.fetchall()
            
            cursor.close()

            return [
                Monitor(
                    id_monitor=l["id_monitor"],
                    departamento=l["departamento"]
                ) for l in linhas
            ]

        finally:
            connect.close()

    def inserir(self, monitor: Monitor) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute(
                    "INSERT INTO monitor (departamento) VALUES (%s)",
                    (monitor.departamento,),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_monitor: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute("DELETE FROM monitor WHERE id_monitor = %s", (id_monitor,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()