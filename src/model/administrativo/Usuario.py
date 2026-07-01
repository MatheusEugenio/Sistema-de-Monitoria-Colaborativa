from dataclasses import dataclass
from typing import Optional

from database.connection import get_connection
import psycopg2.extras

@dataclass
class Usuario:
    id_user: Optional[int] = None
    nome: str
    email: str

class UsuarioRepository:
    
    def buscarPorId(self, id_user: int) -> Optional[Usuario]:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM usuario WHERE id_user = %s", (id_user,))

            linha = cursor.fetchone()
            
            return Usuario(**linha) if linha else None
        finally:
            cursor.close()
            connect.close()

    def existePorEmail(self, email: str) -> bool:
        
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT 1 FROM usuario WHERE email = %s", (email,))

            return cursor.fetchone() is not None
        finally:
            cursor.close()
            connect.close()


    def listarUsuarios(self) -> List[Usuario]:

        connect = get_connection()  
        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM usuario ORDER BY nome")
            
            linhas = cursor.fetchall()
            
            cursor.close()

            return [Usuario(**linha) for linha in linhas]
          
        finally:
            connect.close()

    def inserir(self, usuario: Usuario) -> int:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            try:
                cursor.execute(
                    "INSERT INTO usuario (nome, email) VALUES (%s, %s) RETURNING id_user",
                    (usuario.nome, usuario.email),
                )
                novo_id = cursor.fetchone()["id_user"]
                connect.commit()
                return novo_id

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()   

    def deletar(self, id_user: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            try:
                cursor.execute("delete from usuario where id_user = %s", (id_user,))

                connect.commit()
            except Exception:   
                connect.rollback()
                raise
            
            finally:
                cursor.close()

        finally:
            connect.close()



 