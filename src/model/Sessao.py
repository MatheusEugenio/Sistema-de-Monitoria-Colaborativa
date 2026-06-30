from typing import Optional
from dataclasses import dataclass
from datetime import time

@dataclass
class Sessao:

    id_sessao: Optional[int] = None
    limite_participantes: int
    horario: time
    descricao: str
    # monitoria_id: Optional[int] = None
