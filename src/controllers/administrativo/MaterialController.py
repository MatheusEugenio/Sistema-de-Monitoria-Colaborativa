import pandas as pd

from models import Material, MaterialRepository
import controllers.administrativo.UsuarioController as usuario_controller

_repo = MaterialRepository()

TIPOS_ARQUIVO = ["PDF", "PPTX", "DOC", "ZIP", "PNG", "JPG", "SQL", "TXT", "OUTRO"]

def listar():
    return _repo.listar()


def listar_como_dataframe() -> pd.DataFrame:

    dados = _repo.listar()
    if not dados:
        return pd.DataFrame(columns=["id_material", "titulo", "descricao",
                                      "tipo_arquivo", "link_arquivo", "usuario_id"])
    return pd.DataFrame([m.__dict__ for m in dados])


def opcoes_usuarios() -> dict:
    return usuario_controller.opcoes_usuarios()


def opcoes_tipos() -> list:
    return TIPOS_ARQUIVO

def publicar(titulo: str, descricao: str, tipo_arquivo: str,
             link_arquivo: str, usuario_id: int):

    if not titulo or not link_arquivo:
        return False, "Título e link do arquivo são obrigatórios."

    try:
        
        if _repo.buscarArquivo(titulo, tipo_arquivo, link_arquivo, descricao):
            return False, "Material já publicado." 

        _repo.inserir(Material(
            titulo=titulo,
            descricao=descricao,
            tipo_arquivo=tipo_arquivo,
            link_arquivo=link_arquivo,
            usuario_id=usuario_id,
        ))
        return True, "Material publicado com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_material: int):

    try:
        if _repo.buscarPorId(id_material) is None:
            return False, "Material não encontrado."
            
        _repo.deletar(id_material)
        return True, "Material removido."

    except Exception as erro:
        return False, f"Erro: {erro}"