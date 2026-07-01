from typing import Optional
from dataclasses import dataclass

@dataclass
class Disciplina:

    id_disciplina: Optional[int] = None
    nome: str
    carga_horaria: int
    semestre: str

class DisciplinaRepository(RepositorioBase):

    def buscarDisciplinaPorId(self, id_disciplina: int) -> Optional[Disciplina]:
        
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM disciplinas WHERE id_disciplina = %s", (id_disciplina,))

            linha = cursor.fetchone()
            
            return Disciplina(**linha) if linha else None

        finally:
            cursor.close()
            connect.close()


    def buscarDisciplina(self, nome: str, carga_horaria: int, semestre: str) -> Optional[Disciplina]:

        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM disciplinas WHERE nome = %s AND carga_horaria = %s AND semestre = %s", (nome, carga_horaria, semestre))

            linha = cursor.fetchone()
            
            return Disciplina(**linha) if linha else None

        finally:
            cursor.close()
            connect.close()


    def listar(self) -> List[Disciplina]:

        with get_cursor() as cur:
            cur.execute("SELECT * FROM disciplinas ORDER BY nome")
            linhas = cur.fetchall()
        return [Disciplina(**linha) for linha in linhas]

    def criar(self, disciplina: Disciplina) -> int:

        with get_cursor(commit=True) as cur:
            cur.execute(
                """INSERT INTO disciplinas (nome, codigo)
                   VALUES (%s, %s) RETURNING id""",
                (disciplina.nome, disciplina.codigo),
            )
            return cur.fetchone()["id"]

    def deletar(self, id: int) -> None:
        
            with get_cursor(commit=True) as cur:
                cur.execute("DELETE FROM disciplinas WHERE id = %s", (id,))