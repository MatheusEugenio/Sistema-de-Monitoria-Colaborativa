from typing import Optional, List
from dataclasses import dataclass

import psycopg2.extras
from datetime import date
from database.connection import get_connection

@dataclass
class FilaEspera:

    data_entrada: date
    posicao_na_fila: Optional[int] = None
    id_aluno: int
    id_sessao: int
  
class FilaEsperaRepository:

    def existe(self, id_aluno: int, id_sessao: int) -> bool:
        
        connect = get_connection()
        try:
            cursor = connect.cursor()
            cursor.execute(
                "SELECT 1 FROM fila_espera WHERE id_aluno = %s AND id_sessao = %s",
                (id_aluno, id_sessao)
            )
            return cursor.fetchone() is not None 
        finally:
            connect.close()

    def listar() List[FilaEspera]:

        connect = get_connection()
        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM fila_espera ORDER BY data_entrada")
            
            linhas = cursor.fetchall()
            
            cursor.close()

            filas_espera = []

            for linha in linhas:
                filas_espera.append(FilaEspera(**linha))

            return filas_espera
        finally:
            connect.close()

    def inserir(self, fila_espera: FilaEspera) -> None:

        connect = get_connection()
        
        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    """INSERT INTO fila_espera (data_entrada, id_aluno, id_sessao)
                       VALUES (%s, %s, %s)""",
                    (fila_espera.data_entrada, fila_espera.id_aluno, fila_espera.id_sessao),
                )
                connect.commit()
            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()

    def deletar(self, id_aluno: int, id_sessao: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    "DELETE FROM fila_espera WHERE id_aluno = %s AND id_sessao = %s",
                    (id_aluno, id_sessao),
                )
                connect.commit()
            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()

