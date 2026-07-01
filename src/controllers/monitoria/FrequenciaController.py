import pandas as pd

from models import Frequencia, FrequenciaRepository
import controllers.academico.AlunoController as aluno_controller
import controllers.monitoria.SessaoController as sessao_controller

_repo = FrequenciaRepository()


def listar():
    return _repo.listar()

def listar_como_dataframe() -> pd.DataFrame:
    dados = _repo.listar()
    if not dados:
        return pd.DataFrame(columns=["id_frequencia", "presente", "hora_entrada", "hora_saida", "id_aluno", "id_sessao"])
    return pd.DataFrame([f.__dict__ for f in dados])


def opcoes_alunos() -> dict:
    return aluno_controller.opcoes_alunos()


def opcoes_sessoes() -> dict:
    return sessao_controller.opcoes_sessoes()


def registrar(presente: str, hora_entrada: str, hora_saida: str, id_aluno: int, id_sessao: int):

    if presente not in ("P", "F"):
        return False, "Presença deve ser 'P' ou 'F'."
    if not hora_entrada or not hora_saida:
        return False, "Horários de entrada e saída são obrigatórios."

    try:

        _repo.inserir(Frequencia(
            presente=presente,
            hora_entrada=hora_entrada,
            hora_saida=hora_saida,
            id_aluno=id_aluno,
            id_sessao=id_sessao,
        ))
        return True, "Frequência registrada com sucesso."
    except Exception as erro:

        return False, f"Erro: {erro}"


def remover(id_frequencia: int):

    try:

        if _repo.buscarPorId(id_frequencia) is None:
            return False, "Frequência não encontrada."

        _repo.deletar(id_frequencia)
        return True, "Frequência removida."
        
    except Exception as erro:
        return False, f"Erro: {erro}"