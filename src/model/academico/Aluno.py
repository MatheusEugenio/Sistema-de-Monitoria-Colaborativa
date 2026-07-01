from typing import Optional, List
from dataclasses import dataclass

from sqlalchemy import text

from database.connection import get_session

@dataclass
class Aluno:

    id_aluno: Optional[int] = None 
    matricula: str
    cpf: str
    nome_curso: str

class AlunoRepository:

    def buscarPorIdAluno(self, id_aluno: int) -> Optional[Aluno]:

        session = get_session()

        try:
            resultado = session.execute(text("""
                SELECT
                    id_aluno,
                    matricula,
                    cpf,
                    nome_curso
                FROM aluno
                WHERE id_aluno = :id
                """
            ),
            {"id": id_aluno})

            linha = resultado.mappings().first()
            
            return Aluno(**linha) if linha else None
        finally:
            session.close()
   
    def buscarPorMatricula(self, matricula: str) -> Optional[Aluno]:
        
        session = get_session()

        try:
            resultado = session.execute(text("SELECT * FROM aluno WHERE matricula = :matricula"), {"matricula": matricula})

            linha = resultado.mappings().first()
            
            return Aluno(**linha) if linha else None

        finally:
            session.close()


    def listar(self) -> List[Aluno]:

        session = get_session()

        try:
            resultado = session.execute(text("""
                SELECT
                    id_aluno,
                    matricula,
                    cpf,
                    nome_curso
                FROM aluno
                """))

            linhas = resultado.mappings().all()
            
            return [Aluno(**linha) for linha in linhas]
        finally:
            session.close()


    def inserir(self, aluno: Aluno) -> None:

        session = get_session()

        try:
            session.execute(
                text(
                    """
                    INSERT INTO aluno

                    (matricula, cpf, nome_curso)

                    VALUES

                    (:matricula, :cpf, :curso)
                    """
                ),
                {"matricula": aluno.matricula,
                    "cpf": aluno.cpf,
                    "curso": aluno.nome_curso}
            )

            session.commit()    
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def deletar(self, id_aluno: int) -> None:

        session = get_session()

        try:
            session.execute(
                text(
                    """
                    DELETE
                    FROM aluno
                    WHERE id_aluno = :id
                    """
                ),
                {"id": id_aluno}
            )

            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    