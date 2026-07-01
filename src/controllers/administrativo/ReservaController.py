import pandas as pd

from models import Reserva, ReservaRepository
import controllers.academico.AlunoController as AlunoController
import controllers.monitoria.SessaoController as SessaoController

_repo = ReservaRepository()


def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([r.__dict__ for r in _repo.listar()])


def opcoes_alunos() -> dict:
    return aluno_controller.opcoes_alunos()


def opcoes_sessoes() -> dict:
    return sessao_controller.opcoes_sessoes()


def registrar(data_reserva: str, status: str, id_aluno: int, id_sessao: int):
    try:
            
        _repo.inserir(Reserva(data_reserva=data_reserva, status=status, id_aluno=id_aluno, id_sessao=id_sessao))
        return True, "Reserva registrada."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_reserva: int):

    try:
        if _repo.buscarPorIdReserva(id_reserva) is None:
            return False, "Reserva não encontrada."
            
        _repo.deletar(id_reserva)
        return True, "Reserva removida."

    except Exception as erro:
        return False, f"Erro: {erro}"