from typing import Optional, List
from dataclasses import dataclass
from datetime import date, time

from sqlalchemy import text
from database.connection import get_session

@dataclass
class ValidacaoProfessorMonitor:

    id_validacao: Optional[int] = None
    data_validacao: date
    total_horas: time
    status: str
  
class ValidacaoProfessorMonitorRepository:

    def buscarPorIdValidacao(self, id_validacao: int) -> Optional[ValidacaoProfessorMonitor]:
        
        session = get_session()

        try:
            resultado = session.execute(text("SELECT id_validacao, data_validacao, total_horas, status FROM validacao_professor_monitor WHERE id_validacao = :id"), {"id": id_validacao})
            
            linha = resultado.mappings().first()
            
            return ValidacaoProfessorMonitor(**linha) if linha else None
        finally:
            session.close()

    def listar(self) -> List[ValidacaoProfessorMonitor]:

        session = get_session()

        try:
            resultado = session.execute(text("SELECT id_validacao, data_validacao, total_horas, status FROM validacao_professor_monitor ORDER BY data_validacao DESC"))
            
            linhas = resultado.mappings().all()

            return [ValidacaoProfessorMonitor(**linha) for linha in linhas]
        finally:
            session.close()

    def inserir(self, validacao: ValidacaoProfessorMonitor) -> int:

        session = get_session()

        try:
            resultado = session.execute(text("INSERT INTO validacao_professor_monitor (data_validacao, total_horas, status) VALUES (:data_validacao, :total_horas, :status) RETURNING id_validacao"), {"data_validacao": validacao.data_validacao, "total_horas": validacao.total_horas, "status": validacao.status})

            novo_id = resultado.scalar()

            session.commit()

            return novo_id

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_validacao: int) -> None:

        session = get_session()

        try:
            session.execute(text("DELETE FROM validacao_professor_monitor WHERE id_validacao = :id"), {"id": id_validacao})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    