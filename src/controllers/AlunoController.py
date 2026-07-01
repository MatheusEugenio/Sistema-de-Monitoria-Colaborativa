import pandas as pd

from models import Aluno, AlunoRepository
import controllers.UsuarioController as usuario_controller

_repo = AlunoRepository()

def listar():
    return _repo.listar()

#como se fosse em json
def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([a.__dict__ for a in _repo.listar()])


def opcoes_alunos() -> dict:
    return {f"Aluno #{a.id_aluno} (matrícula {a.matricula})": a.id_aluno for a in _repo.listar()}


def opcoes_usuarios_disponiveis() -> dict:

    """Usuários que ainda podem virar Aluno (auxiliar pro formulário)."""
    return usuario_controller.opcoes_usuarios()


def cadastrar(matricula: int, cpf: str, nome_curso: str, id_usuario: int):

    if not cpf or not nome_curso:
        return False, "CPF e curso são obrigatórios."
    
    try:
        if _repo.buscarPorMatricula(matricula):
            return False, "Aluno com a mesma matrícula já cadastrado."

        if _repo.buscarPorIdUsuario(id_usuario):
            return False, "Usuário já cadastrado como aluno."

        _repo.inserir(Aluno(matricula=matricula, cpf=cpf, nome_curso=nome_curso, id_usuario=id_usuario))
        
        return True, "Aluno cadastrado com sucesso."
    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_aluno: int):
    try:

        if not _repo.buscarPorIdUsuario(id_aluno):
            return False, "Aluno não encontrado."

        _repo.deletar(id_aluno)
        return True, "Aluno removido."
        
    except Exception as erro:
        return False, f"Erro: {erro}"