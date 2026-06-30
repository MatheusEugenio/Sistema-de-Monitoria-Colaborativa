from typing import Optional
from dataclasses import dataclass


@dataclass
class Material:

    id_material: Optional[int] = None
    #usuario_id: Optional[int] = None
    tipo-arquivo: str
    link_arquivo: str
    descricao: str
    titulo: str