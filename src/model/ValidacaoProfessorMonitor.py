from typing import Optional
from dataclasses import dataclass
from datetime import date, time

@dataclass
class ValidacaoProfessorMonitor:

    id_validacao: Optional[int] = None
    data_validacao: date
    total_horas: time
    status: str
    # professor_id: int
    # monitor_id: int
    