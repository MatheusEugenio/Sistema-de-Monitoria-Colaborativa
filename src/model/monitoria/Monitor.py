from typing import Optional, List
from dataclasses import dataclass

from sqlalchemy import text
from database.connection import get_session

@dataclass
class Monitor:

    id_monitor: Optional[int] = None
    departamento: str

class MonitorRepository:

    def buscarPorIdMonitor(self, id_monitor: int) -> Optional[Monitor]:
        
        session = get_session()
        
        try:
            
            resultado = session.execute(text("SELECT id_monitor, departamento FROM monitor WHERE id_monitor = :id_monitor"), {"id_monitor": id_monitor})
            
            linha = resultado.mappings().first()

            return Monitor(**linha) if linha else None

        finally:
            session.close()

    def listar(self) -> List[Monitor]:
        
        session = get_session()

        try:
            resultado = session.execute(text("SELECT id_monitor, departamento FROM monitor"))
            
            linhas = resultado.mappings().all()
            
            return [Monitor(**linha) for linha in linhas]

        finally:
            session.close()

    def inserir(self, monitor: Monitor) -> None:

        session = get_session()
        
        try:

            existe = session.execute(text("SELECT 1 FROM monitor WHERE id_monitor = :id_monitor"), {"id_monitor": monitor.id_monitor}).first()
            
            if existe:
                raise ValueError("Monitor já existe.")
            
            session.execute(text("INSERT INTO monitor (departamento) VALUES (:departamento)"), {"departamento": monitor.departamento})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_monitor: int) -> None:

        session = get_session()
        
        try:
            session.execute(text("DELETE FROM monitor WHERE id_monitor = :id_monitor"), {"id_monitor": id_monitor})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()