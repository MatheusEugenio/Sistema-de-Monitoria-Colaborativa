import pandas as pd
from models import FilaEspera, FilaEsperaRepository
import controllers.AlunoController as aluno_controller
import controllers.SessaoController as sessao_controller

_repo = FilaEsperaRepository()

def listar():
    return _repo.listar()

def listar_como_dataframe() -> pd.DataFrame:
    dados = _repo.listar()
    if not dados:
        return pd.DataFrame(columns=["data_entrada", "posicao_na_fila", "id_aluno", "id_sessao"])
    return pd.DataFrame([f.__dict__ for f in dados])

def opcoes_alunos() -> dict:
    return aluno_controller.opcoes_alunos()

def opcoes_sessoes() -> dict:
    return sessao_controller.opcoes_sessoes()

def cadastrar(data_entrada: date, id_aluno: int, id_sessao: int):
    
    if not data_entrada:
        return False, "A data de entrada é obrigatória."
    if not id_aluno or not id_sessao:
        return False, "Aluno e Sessão são obrigatórios."

    try:

        if _repo.existe(id_aluno, id_sessao):
            return False, "Aluno já está na fila desta sessão."

        _repo.inserir(FilaEspera(
            data_entrada=data_entrada,
            id_aluno=id_aluno,
            id_sessao=id_sessao
        ))
        return True, "Aluno adicionado à fila de espera com sucesso."

    except Exception as erro:
        return False, f"Erro ao cadastrar na fila: {erro}"

def remover(id_aluno: int, id_sessao: int):
    try:
        
        if not _repo.existe(id_aluno, id_sessao):
            return False, "Aluno não está na fila desta sessão."

        _repo.deletar(id_aluno, id_sessao)
        return True, "Aluno removido da fila de espera."
    except Exception as erro:
        return False, f"Erro ao remover da fila: {erro}"