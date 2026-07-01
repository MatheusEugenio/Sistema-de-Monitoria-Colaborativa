import pandas as pd

from models import Validacao, ValidacaoRepository
import controllers.administrativo.ProfessorController as professor_controller
import controllers.monitoria.MonitorController as monitor_controller

_repo = ValidacaoRepository()

STATUS_OPCOES = ["Pendente", "Aprovado", "Rejeitado"]

def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    dados = _repo.listar()
    if not dados:
        return pd.DataFrame(columns=["id_validacao", "data_validacao", "total_horas", "status_validacao", "id_professor", "id_monitor"])
    return pd.DataFrame([v.__dict__ for v in dados])


def opcoes_professores() -> dict:
    return professor_controller.opcoes_professores()


def opcoes_monitores() -> dict:
    return monitor_controller.opcoes_monitores()


def opcoes_status() -> list:
    return STATUS_OPCOES


def registrar(data_validacao: str, total_horas: int, status_validacao: str,
              id_professor: int, id_monitor: int):

    if not data_validacao:
        return False, "Data de validação é obrigatória."

    if total_horas <= 0:
        return False, "Total de horas deve ser maior que zero."

     if status_validacao not in STATUS_OPCOES:
            return False, "Status de validação inválido."

    try:
        
        _repo.inserir(Validacao(
            data_validacao=data_validacao,
            total_horas=total_horas,
            status_validacao=status_validacao,
            id_professor=id_professor,
            id_monitor=id_monitor,
        ))

        return True, "Validação registrada com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_validacao: int):

    try:

        if not _repo.buscarPorIdValidacao(id_validacao):
            return False, "Validação não encontrada."

        _repo.deletar(id_validacao)
        return True, "Validação removida."

    except Exception as erro:
        return False, f"Erro: {erro}"