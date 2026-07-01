from typing import List, Optional
from dataclasses import dataclass

from sqlalchemy import text
from database.connection import get_session

@dataclass
class Monitoria:

    id_monitoria: Optional[int] = None
    monitor_id: int 
    disciplina_id: int 


class MonitoriaRepository:

   def buscarPorIdMonitoria(self, id_monitoria: int) -> Optional[Monitoria]:
        
        session = get_session()
        
        try:

            resultado = session.execute(text("SELECT id AS id_monitoria, monitor_id, disciplina_id FROM monitorias WHERE id = :id"), {"id": id_monitoria})
            
            linha = resultado.mappings().first()

            return Monitoria(**linha) if linha else None

        finally:
            session.close()

    def listar(self) -> List[Monitoria]:
        
        session = get_session()
        
        try:
            resultado = session.execute(text("SELECT m.id AS id_monitoria, m.monitor_id, m.disciplina_id FROM monitorias m JOIN usuarios u ON u.id = m.monitor_id JOIN disciplinas d ON d.id = m.disciplina_id ORDER BY d.nome"))
            
            linhas = resultado.mappings().all()

            return [Monitoria(**linha) for linha in linhas]

        finally:
            session.close()

    def inserir(self, monitoria: Monitoria) -> int:
        session = get_session()
        try:
            
            existe = session.execute(text("SELECT 1 FROM monitorias WHERE id = :id"), {"id": monitoria.id_monitoria}).first()
            
            if existe:
                raise ValueError(f"Monitoria com ID {monitoria.id_monitoria} já existe.")
            
            resultado = session.execute(text("INSERT INTO monitorias (monitor_id, disciplina_id) VALUES (:monitor_id, :disciplina_id) RETURNING id"), {"monitor_id": monitoria.monitor_id, "disciplina_id": monitoria.disciplina_id})
            
            novo_id = resultado.scalar()

            session.commit()
            
            return novo_id

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_monitoria: int) -> None:
        
        session = get_session()
        
        try:
            
            session.execute(text("DELETE FROM monitorias WHERE id = :id"), {"id": id_monitoria})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()