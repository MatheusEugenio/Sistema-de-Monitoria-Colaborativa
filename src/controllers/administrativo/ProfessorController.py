import pandas as pd

from models import Professor, ProfessorRepository
import controllers.administrativo.UsuarioController as usuario_controller

_repo = ProfessorRepository()

def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([p.__dict__ for p in _repo.listar()])


def opcoes_professores() -> dict:
    return {f"Professor #{p.id_professor} ({p.departamento})": p.id_professor for p in _repo.listar()}


def opcoes_usuarios_disponiveis() -> dict:
    return usuario_controller.opcoes_usuarios()


def cadastrar(departamento: str, usuario_id: int):
    
    if not departamento:
        return False, "Departamento é obrigatório."

    try:
        _repo.inserir(Professor(departamento=departamento, usuario_id=usuario_id))

        return True, "Professor cadastrado com sucesso."
    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_professor: int):

    try:

        if not _repo.buscarPorIdProfessor(id_professor):
            return False, "Professor não encontrado."
            
        _repo.deletar(id_professor)
        return True, "Professor removido."

    except Exception as erro:
        return False, f"Erro: {erro}"