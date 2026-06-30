# from typing import Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class FilaEspera:

    data_entrada: date
    posicao_na_fila: int
    # aluno_id: Optional[int] = None
    # sessao_id: Optional[int] = None