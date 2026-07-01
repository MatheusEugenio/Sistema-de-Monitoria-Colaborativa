from typing import Optional, List
from dataclasses import dataclass
from datetime import date

from sqlalchemy import text
from database.connection import get_session

@dataclass
class FilaEspera:

    data_entrada: date
    posicao_na_fila: Optional[int] = None
    id_aluno: int
    id_sessao: int
  
class FilaEsperaRepository:

    def existe(self, id_aluno: int, id_sessao: int) -> bool:
        
        session = get_session()

        try:
            resultado = session.execute(text("SELECT 1 FROM fila_espera WHERE id_aluno = :id_aluno AND id_sessao = :id_sessao"), {"id_aluno": id_aluno, "id_sessao": id_sessao})
            
            return resultado.first() is not None
        finally:
            session.close()

    def listar(self) -> List[FilaEspera]:
        
        session = get_session()

        try:
            resultado = session.execute(text("SELECT data_entrada, posicao_na_fila, id_aluno, id_sessao FROM fila_espera ORDER BY data_entrada"))
            
            linhas = resultado.mappings().all()

            return [FilaEspera(**linha) for linha in linhas]
        finally:
            session.close()

    def inserir(self, fila_espera: FilaEspera) -> None:

        session = get_session()

        try:

            session.execute(text("INSERT INTO fila_espera (data_entrada, id_aluno, id_sessao) VALUES (:data_entrada, :id_aluno, :id_sessao)"), {"data_entrada": fila_espera.data_entrada, "id_aluno": fila_espera.id_aluno, "id_sessao": fila_espera.id_sessao})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_aluno: int, id_sessao: int) -> None:

        session = get_session()

        try:

            session.execute(text("DELETE FROM fila_espera WHERE id_aluno = :id_aluno AND id_sessao = :id_sessao"), {"id_aluno": id_aluno, "id_sessao": id_sessao})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()