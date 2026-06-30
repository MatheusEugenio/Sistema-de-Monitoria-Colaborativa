from datetime import time
from enum import Enum
from typing import Optional
from dataclasses import dataclass

class Presenca(Enum):
    PRESENTE = "P"
    FALTA = "F"

@dataclass
class Frequencia:

    id_frequencia: Optional[int] = None
   # aluno_id: int
   # sessao_id: int
    hora_saida: time
    hora_entrada: time
    presente: Presenca

