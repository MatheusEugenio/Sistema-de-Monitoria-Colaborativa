from typing import Optional, List
from dataclasses import dataclass
from datetime import time

from sqlalchemy import text
from database.connection import get_session

@dataclass
class Sessao:

    id_sessao: Optional[int] = None
    limite_participantes: int
    horario: time
    descricao: str

class SessaoRepository:

     def buscarPorIdSessao(self, id_sessao: int) -> Optional[Sessao]:
       
        session = get_session()
       
        try:
           
            resultado = session.execute(text("SELECT id_sessao, limite_participantes, horario, descricao FROM sessao WHERE id_sessao = :id_sessao"), {"id_sessao": id_sessao})
           
            linha = resultado.mappings().first()
            
            return Sessao(**linha) if linha else None
        finally:
            session.close()

    def buscarSessao(self, id_sessao: int, horario: time) -> Optional[Sessao]:
       
        session = get_session()
       
        try:
            resultado = session.execute(text("SELECT id_sessao, limite_participantes, horario, descricao FROM sessao WHERE id_sessao = :id_sessao AND horario = :horario"), {"id_sessao": id_sessao, "horario": horario})
           
            linha = resultado.mappings().first()
           
            return Sessao(**linha) if linha else None
        finally:
            session.close()

     def listar(self) -> List[Sessao]:
        
        session = get_session()
        
        try:
            
            resultado = session.execute(text("SELECT id_sessao, limite_participantes, horario, descricao FROM sessao ORDER BY horario"))
            
            linhas = resultado.mappings().all()
            
            return [Sessao(**linha) for linha in linhas]
        finally:
            session.close()

    def inserir(self, sessao: Sessao) -> None:
       
        session = get_session()
        
        try:
            
            existe = session.execute(text("SELECT 1 FROM sessao WHERE id_sessao = :id_sessao AND horario = :horario"), {"id_sessao": sessao.id_sessao, "horario": sessao.horario}).first()
            
            if existe:
                raise ValueError(f"Sessão com ID {sessao.id_sessao} e horário {sessao.horario} já existe.")
           
            session.execute(text("INSERT INTO sessao (limite_participantes, horario, descricao) VALUES (:limite_participantes, :horario, :descricao)"), {"limite_participantes": sessao.limite_participantes, "horario": sessao.horario, "descricao": sessao.descricao})
           
            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_sessao: int) -> None:

        session = get_session()

        try:

            session.execute(text("DELETE FROM sessao WHERE id_sessao = :id_sessao"), {"id_sessao": id_sessao})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()