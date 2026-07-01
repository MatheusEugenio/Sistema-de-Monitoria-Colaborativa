from typing import Optional, List
from dataclasses import dataclass
import psycopg2.extras
from database.connection import get_connection

@dataclass
class Aluno:

    id_aluno: Optional[int] = None 
    matricula: str
    cpf: str
    nome_curso: str

class AlunoRepository:

    def buscarPorIdUsuario(self, id_aluno: int) -> Optional[Aluno]:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM aluno WHERE id_aluno = %s", (id_aluno,))

            linha = cursor.fetchone()
            
            return Aluno(**linha) if linha else None
        finally:
            cursor.close()
            connect.close()
   
    def buscarPorMatricula(self, matricula: str) -> Optional[Aluno]:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM aluno WHERE matricula = %s", (matricula,))

            linha = cursor.fetchone()
            
            return Aluno(**linha) if linha else None
        finally:
            cursor.close()
            connect.close()


    def listar(self) -> List[Aluno]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT id_aluno, matricula, cpf, nome_curso FROM aluno")

            linhas = cursor.fetchall()
            cursor.close()

            return [
                Aluno(
                    id_aluno=l["id_aluno"],
                    matricula=l["matricula"],
                    cpf=l["cpf"],
                    nome_curso=l["nome_curso"]
                ) for l in linhas
            ]

        finally:
            connect.close()

    def inserir(self, aluno: Aluno) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    """INSERT INTO aluno (matricula, cpf, nome_curso) 
                       VALUES (%s, %s, %s)""",
                    (aluno.matricula, aluno.cpf, aluno.nome_curso),
                )
                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()
        finally:
            connect.close()

    def deletar(self, id_aluno: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()
            try:
                cursor.execute("DELETE FROM aluno WHERE id_aluno = %s", (id_aluno,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise
                
            finally:
                cursor.close()
        finally:
            connect.close()
    