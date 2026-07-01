import pandas as pd

from models import Monitor, MonitorRepository
import controllers.AlunoController as aluno_controller

_repo = MonitorRepository()


def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([m.__dict__ for m in _repo.listar()])


def opcoes_monitores() -> dict:
    return {f"Monitor #{m.id_monitor} ({m.departamento})": m.id_monitor for m in _repo.listar()}


def opcoes_alunos_disponiveis() -> dict:
    return aluno_controller.opcoes_alunos()


def cadastrar(departamento: str):

    if not departamento:
        return False, "Departamento é obrigatório."

    try:

        _repo.inserir(Monitor(departamento=departamento))
        return True, "Monitor cadastrado com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_monitor: int):

    try:
        if _repo.buscarPorIdMonitor(id_monitor) is None:
            return False, "Monitor não encontrado." 

        _repo.deletar(id_monitor)
        return True, "Monitor removido."

    except Exception as erro:
        return False, f"Erro: {erro}"