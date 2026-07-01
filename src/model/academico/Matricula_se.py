from typing import List, Optional
from dataclasses import dataclass

import psycopg2.extras
from database.connectection import get_connectection

@dataclass
class Matricula_se:

    aluno_id: Optional[int] = None
    disciplina_id: Optional[int] = None
    turma_id: Optional[int] = None

class Matricula_seRepository:

    def 


    def listar(self) -> List[MatriculaSe]:

        connect = get_connectection()
        
        try:

            cursor = connect.cursorsor(cursorsor_factory=psycopg2.extras.RealDictcursorsor)

            cursor.execute("SELECT * FROM matricula_se ORDER BY id_aluno")

            linhas = cursor.fetchall()
            cursor.close()

            matriculas_se = []

            for linha in linhas:
                matriculas_se.append(MatriculaSe(**linha))
            
            return matriculas_se
        finally:
            connect.close()
 
    def criar(self, matricula_se: MatriculaSe) -> None:
        
        connect = get_connectection()
        
        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    """INSERT INTO matricula_se (id_aluno, id_disciplina, id_turma)
                       VALUES (%s, %s, %s)""",
                    (matricula_se.id_aluno, matricula_se.id_disciplina, matricula_se.id_turma),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()
 
    def deletar(self, id_aluno: int, id_disciplina: int, id_turma: int) -> None:
        
        connect = get_connectection()
        
        try:
            cursor = connect.cursor()
            try:
                cursor.execute(
                    """DELETE FROM matricula_se
                       WHERE id_aluno = %s AND id_disciplina = %s AND id_turma = %s""",
                    (id_aluno, id_disciplina, id_turma),
                )
                connect.commit()
            except Exception:
                connect.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connect.close()
 