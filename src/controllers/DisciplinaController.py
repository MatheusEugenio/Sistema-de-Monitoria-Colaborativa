import pandas as pd

from models import Disciplina, DisciplinaRepository

repo = DisciplinaRepository()

def listar():
    return repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([d.__dict__ for d in repo.listar()])


def opcoes_disciplinas() -> dict:
    return {f"{d.nome} (#{d.id_disciplina})": d.id_disciplina for d in repo.listar()}


def cadastrar(nome: str, carga_horaria: int, semestre: str):

    if not nome or not semestre:
        return False, "Nome e semestre são obrigatórios."
    
    try:

        if repo.buscarDisciplina(nome=nome, carga_horaria=carga_horaria, semestre=semestre):
            raise ValueError("Disciplina já existe.")

        repo.inserir(Disciplina(nome=nome, carga_horaria=carga_horaria, semestre=semestre))
        return True, "Disciplina criada com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_disciplina: int):

    try:
        if not repo.buscarDisciplinaPorId(id_disciplina):
            raise ValueError("Disciplina não encontrada.") 

        repo.deletar(id_disciplina)
        return True, "Disciplina removida."

    except Exception as erro:
        return False, f"Erro: {erro}"