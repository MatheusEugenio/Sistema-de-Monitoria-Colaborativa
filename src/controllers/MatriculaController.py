import pandas as pd

from models import MatriculaSe, MatriculaSeRepository
import controllers.AlunoController as aluno_controller
import controllers.DisciplinaController as disciplina_controller
import controllers.TurmaController as turma_controller

_repo = MatriculaSeRepository()


def listar():
    return _repo.listar()

def listar_como_dataframe() -> pd.DataFrame:
    dados = _repo.listar()
    if not dados:
        return pd.DataFrame(columns=["id_aluno", "id_disciplina", "id_turma"])
    return pd.DataFrame([m.__dict__ for m in dados])


def opcoes_alunos() -> dict:
    return aluno_controller.opcoes_alunos()


def opcoes_disciplinas() -> dict:
    return disciplina_controller.opcoes_disciplinas()


def opcoes_turmas() -> dict:
    return turma_controller.opcoes_turmas()


def matricular(id_aluno: int, id_disciplina: int, id_turma: int):

    try:

        _repo.inserir(MatriculaSe(id_aluno=id_aluno, id_disciplina=id_disciplina, id_turma=id_turma))
        return True, "Aluno matriculado com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_aluno: int, id_disciplina: int, id_turma: int):

    try:
        _repo.deletar(id_aluno, id_disciplina, id_turma)
        return True, "Matrícula removida."
    except Exception as erro:
        return False, f"Erro: {erro}"