from typing import Optional
from dataclasses import dataclass
from datetime import time, date

class DiaSemana(IntEnum):
    SEGUNDA = 0
    TERCA = 1
    QUARTA = 2
    QUINTA = 3
    SEXTA = 4
    SABADO = 5
    DOMINGO = 6

@dataclass
class Disponibilidade:

    id_disponibilidade: Optional[int] = None
    horario_inicio: time
    horario_fim: time
    data_inicio: date
    data_fim: date
    dia_semana: DiaSemana
    # monitor_id: int