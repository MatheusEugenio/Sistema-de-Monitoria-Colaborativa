from typing import List, Optional
from dataclasses import dataclass
import psycopg2.extras
from database.connectection import get_connection

@dataclass
class Monitoria:

    id_monitoria: Optional[int] = None
    monitor_id: int 
    disciplina_id: int 


class MonitoriaRepository:

    def buscarPorIdMonitoria(self, id_monitoria: int) -> Optional[Monitoria]:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM monitorias WHERE id = %s", (id_monitoria,))

            linha = cursor.fetchone()
            
            return Monitoria(**linha) if linha else None
        finally:
            cursor.close()
            connect.close()
   
    def listar(self) -> List[Monitoria]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute("""
                SELECT m.id, m.monitor_id, m.disciplina_id
                FROM monitorias m
                JOIN usuarios u ON u.id = m.monitor_id
                JOIN disciplinas d ON d.id = m.disciplina_id
                ORDER BY d.nome
            """)

            linhas = cursor.fetchall()
            cursor.close()

            return [
                Monitoria(
                    id_monitoria=l["id"],
                    monitor_id=l["monitor_id"],
                    disciplina_id=l["disciplina_id"],
                ) for l in linhas
            ]

        finally:
            connect.close()

    def criar(self, monitoria: Monitoria) -> int:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
            if self.buscarPorIdMonitoria(monitoria.id_monitoria): 
                raise ValueError(f"Monitoria com ID {monitoria.id_monitoria} já existe.")
                
            try:
                cursor.execute(
                    """INSERT INTO monitorias (monitor_id, disciplina_id)
                       VALUES (%s, %s) RETURNING id""",
                    (monitoria.monitor_id, monitoria.disciplina_id),
                )

                novo_id = cursor.fetchone()["id"]

                connect.commit()

                return novo_id
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
                cursor.execute("DELETE FROM monitorias WHERE id = %s", (id_monitor,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()
        finally:
            connect.close()