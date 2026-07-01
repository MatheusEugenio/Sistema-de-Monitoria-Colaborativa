import pandas as pd

from models import Usuario, UsuarioRepository

_repo = UsuarioRepository()


def listar():
    return _repo.listarUsuarios()

#como se fosse em json
def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([u.__dict__ for u in _repo.listarUsuarios()])


def opcoes_usuarios() -> dict:
    opcoes = {}

    for u in _repo.listarUsuarios():
        chave = f"{u.nome} (#{u.id_user})"
        opcoes[chave] = u.id_user

    return opcoes


def cadastrar(nome: str, email: str):

    if not nome or not email:
        return False, "Nome e email são obrigatórios."

    try:
        if _repo.existePorEmail(email):
            return False, "Usuário com o mesmo email já cadastrado."

        _repo.inserir(Usuario(nome=nome, email=email))
        return True, "Usuário criado com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_user: int):
    try:

        if _repo.buscarPorId(id_user) is None:
            return False, "Usuário não presente no banco, impossível remover."
            
        _repo.deletar(id_user)
        return True, "Usuário removido."
        
    except Exception as erro:
        return False, f"Erro: {erro}"