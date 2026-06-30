from typing import Optional
from dataclasses import dataclass
from datetime import date, time

@dataclass
class Aviso:

    id_aviso: Optional[int] = None
    titulo: str
    descricao: str
    data_publicacao: date
    # usuario_id: Optional[int] = None