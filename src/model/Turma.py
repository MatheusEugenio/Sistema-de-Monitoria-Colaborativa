from typing import Optional
from dataclasses import dataclass
from datetime import time

@dataclass
class Turma:

    id_turma: Optional[int] = None
    semestre: str
    codigo: str
    # disciplina_id: Optional[int] = None
    horario: time