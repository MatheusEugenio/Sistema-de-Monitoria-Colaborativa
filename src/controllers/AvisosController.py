import pandas as pd

from models import Aviso, AvisoRepository
import controllers.academico.UsuarioController as usuario_controller

_repo = AvisoRepository()

def listar():
    return _repo.listar()

def listar_como_dataframe() -> pd.DataFrame:
    return pd.DataFrame([a.__dict__ for a in _repo.listar()])


def opcoes_usuarios() -> dict:
    return usuario_controller.opcoes_usuarios()


def publicar(titulo: str, conteudo: str, data_publicacao: str, usuario_id: int):

    if not titulo or not conteudo:
        return False, "Título e conteúdo são obrigatórios."

    try:

        if _repo.buscarAviso(titulo, conteudo):
            return False, "Aviso com o mesmo título e conteúdo já existe."

        _repo.inserir(Aviso(titulo=titulo, conteudo=conteudo,
                           data_publicacao=data_publicacao, usuario_id=usuario_id))
        return True, "Aviso publicado."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_aviso: int):

    try:
        if not _repo.buscarAvisoPorId(id_aviso):
            return False, "Aviso não encontrado."

        _repo.deletar(id_aviso)
        return True, "Aviso removido."

    except Exception as erro:
        return False, f"Erro: {erro}"