import pandas as pd

from models import Turma, TurmaRepository
import controllers.academico.DisciplinaController as disciplina_controller

_repo = TurmaRepository()


def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([t.__dict__ for t in _repo.listar()])


def opcoes_turmas() -> dict:
    return {f"{t.codigo} (#{t.id_turma})": t.id_turma for t in _repo.listar()}


def opcoes_disciplinas() -> dict:
    return disciplina_controller.opcoes_disciplinas()


def cadastrar(semestre: str, codigo: str, disciplina_id: int, horario: str):
    
    if not codigo or not horario:
        return False, "Código e horário são obrigatórios."

    try:

        if _repo.buscarTurma(semestre, codigo):
            return False, "Turma já cadastrada."

        _repo.inserir(Turma(semestre=semestre, codigo=codigo, disciplina_id=disciplina_id, horario=horario))
        return True, "Turma criada com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_turma: int):

    try:
        if not _repo.buscarPorIdTurma(id_turma):
            return False, "Turma não encontrada."
            
        _repo.deletar(id_turma)
        return True, "Turma removida."

    except Exception as erro:
        return False, f"Erro: {erro}"