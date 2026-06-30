from typing import Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class Reserva:

    id_reserva: Optional[int] = None
    data_reserva: datetime
    status: bool
    # aluno_id: Optional[int] = None
    # sessao_id: Optional[int] = None