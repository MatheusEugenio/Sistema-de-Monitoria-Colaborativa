from typing import List, Optional
from dataclasses import dataclass
import psycopg2.extras
from database.connectection import get_connectection

@dataclass
class Material:
    id_material: Optional[int] = None
    tipo_arquivo: str
    link_arquivo: Optional[str] = None
    descricao: str
    titulo: str

class MaterialRepository:

    def buscarPorId(self, id_material: int) -> Optional[Material]:
            
        connect = get_connectection()
        
        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute(
                "SELECT * FROM material WHERE id_material = %s",
                (id_material,)
            )

            linha = cursor.fetchone()
            cursor.close()

            return Material(**linha) if linha else None
        finally:
            connect.close()

    def buscarArquivo(self, titulo, tipo_arquivo, link_arquivo, descricao) -> Optional[Material]:
        connect = get_connectection()
        
        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute(
                "SELECT * FROM material WHERE titulo = %s AND tipo_arquivo = %s AND link_arquivo = %s AND descricao = %s",
                (titulo, tipo_arquivo, link_arquivo, descricao)
            )

            linha = cursor.fetchone()
            cursor.close()

            return Material(**linha) if linha else None
        finally:
            connect.close()


    def listar(self) -> List[Material]:
        
        connect = get_connectection()
        
        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT * FROM material ORDER BY id_material")

            linhas = cursor.fetchall()
            cursor.close()
            
            materiais = []

            for linha in linhas:
                materiais.append(Material(**linha))
                
            return materiais
        finally:
            connect.close()

    def inserir(self, material: Material) -> None:

        connect = get_connectection()

        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    """INSERT INTO material (tipo_arquivo, link_arquivo, descricao, titulo) 
                       VALUES (%s, %s, %s, %s)""",
                    (material.tipo_arquivo, material.link_arquivo, material.descricao, material.titulo),
                )

                connect.commit()
            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()

    def deletar(self, id_material: int) -> None:

        connect = get_connectection()

        try:
            cursor = connect.cursor()
            try:
                cursor.execute("DELETE FROM material WHERE id_material = %s", (id_material,))

                connect.commit()
            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()