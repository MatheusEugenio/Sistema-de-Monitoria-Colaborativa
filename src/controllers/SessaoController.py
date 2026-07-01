import pandas as pd

from models import Sessao, SessaoRepository
import controllers.MonitoriaController as monitoria_controller

_repo = SessaoRepository()

def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([s.__dict__ for s in _repo.listar()])


def opcoes_sessoes() -> dict:
    return {f"Sessão #{s.id_sessao} - {s.data}": s.id_sessao for s in _repo.listar()}


def opcoes_monitorias() -> dict:
    return monitoria_controller.opcoes_monitorias()


def cadastrar(limite_participantes: int, horario: str, descricao: str, data: str, id_monitoria: int):

    if not descricao or not data or not horario:
        return False, "Descrição, data e horário são obrigatórios."

    try:

        _repo.criar(Sessao(
            limite_participantes=limite_participantes, horario=horario,
            descricao=descricao, data=data, id_monitoria=id_monitoria,
        ))
        return True, "Sessão criada com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_sessao: int):

    try:
        if not _repo.buscarPorIdSessao(id_sessao):
            return False, "Sessão não encontrada."
            
        _repo.deletar(id_sessao)
        return True, "Sessão removida."
        
    except Exception as erro:
        return False, f"Erro: {erro}"