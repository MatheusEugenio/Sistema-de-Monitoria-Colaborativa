import pandas as pd

from models import Ministra, MinistraRepository
import controllers.administrativo.ProfessorController as professor_controller
import controllers.academico.DisciplinaController as disciplina_controller

_repo = MinistraRepository()

def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    dados = _repo.listar()
    if not dados:
        return pd.DataFrame(columns=["professor_id", "disciplina_id"])
    return pd.DataFrame([m.__dict__ for m in dados])


def opcoes_professores() -> dict:
    return professor_controller.opcoes_professores()


def opcoes_disciplinas() -> dict:
    return disciplina_controller.opcoes_disciplinas()


def associar(professor_id: int, disciplina_id: int):

    try:    
        if _repo.jaExiste(professor_id, disciplina_id):
            return False, "Esta associação já existe."

        _repo.inserir(Ministra(professor_id=professor_id, disciplina_id=disciplina_id))
        return True, "Associação Professor → Disciplina registrada."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(professor_id: int, disciplina_id: int):

    try:

        if not _repo.jaExiste(professor_id, disciplina_id):
            return False, "Esta associação não existe."
            
        _repo.deletar(professor_id, disciplina_id)
        return True, "Associação removida."

    except Exception as erro:
        return False, f"Erro: {erro}"