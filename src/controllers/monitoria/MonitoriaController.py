import pandas as pd

from models import Monitoria, MonitoriaRepository
import controllers.monitoria.MonitorController as monitor_controller
import controllers.academico.DisciplinaController as disciplina_controller

_repo = MonitoriaRepository()

def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([m.__dict__ for m in _repo.listar()])


def opcoes_monitorias() -> dict:
    return {f"Monitoria #{m.id_monitoria}": m.id_monitoria for m in _repo.listar()}


def opcoes_monitores() -> dict:
    return monitor_controller.opcoes_monitores()


def opcoes_disciplinas() -> dict:
    return disciplina_controller.opcoes_disciplinas()


def cadastrar(id_monitor: int, id_disciplina: int):

    try:
        _repo.inserir(Monitoria(id_monitor=id_monitor, id_disciplina=id_disciplina))
        return True, "Monitoria criada com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_monitoria: int):

    try:

        if _repo.buscarPorIdMonitoria(id_monitoria) is None:
            return False, "Monitoria não encontrada."
            
        _repo.deletar(id_monitoria)
        return True, "Monitoria removida."

    except Exception as erro:
        return False, f"Erro: {erro}"