from typing import Optional, List
from dataclasses import dataclass
from datetime import date

from sqlalchemy import text
from database.connection import get_session

@dataclass
class Aviso:

    id_aviso: Optional[int] = None
    titulo: str
    descricao: str
    data_publicacao: date

class AvisoRepository:

    def buscarAvisoPorId(self, id_aviso: int) -> Optional[Aviso]:
        
        session = get_session()
        
        try:
            resultado = session.execute(text("SELECT id_aviso, titulo, descricao, data_publicacao FROM aviso WHERE id_aviso = :id_aviso"), {"id_aviso": id_aviso})
            
            linha = resultado.mappings().first()
            
            return Aviso(**linha) if linha else None
        finally:
            session.close()

    def buscarAviso(self, titulo: str, descricao: str) -> Optional[Aviso]:
        
        session = get_session()
        
        try:
            resultado = session.execute(text("SELECT id_aviso, titulo, descricao, data_publicacao FROM aviso WHERE titulo = :titulo AND descricao = :descricao"), {"titulo": titulo, "descricao": descricao})
            
            linha = resultado.mappings().first()
            
            return Aviso(**linha) if linha else None
        finally:
            session.close()

    def listar(self) -> List[Aviso]:
        
        session = get_session()
        
        try:
            resultado = session.execute(text("SELECT id_aviso, titulo, descricao, data_publicacao FROM aviso ORDER BY data_publicacao DESC"))
           
            linhas = resultado.mappings().all()
           
            return [Aviso(**linha) for linha in linhas]
        finally:
            session.close()

    def inserir(self, aviso: Aviso) -> None:
       
        session = get_session()
        
        try:
            
            session.execute(text("INSERT INTO aviso (titulo, descricao, data_publicacao) VALUES (:titulo, :descricao, :data_publicacao)"), {"titulo": aviso.titulo, "descricao": aviso.descricao, "data_publicacao": aviso.data_publicacao})
            
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_aviso: int) -> None:
        
        session = get_session()
        
        try:
            
            session.execute(text("DELETE FROM aviso WHERE id_aviso = :id_aviso"), {"id_aviso": id_aviso})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()