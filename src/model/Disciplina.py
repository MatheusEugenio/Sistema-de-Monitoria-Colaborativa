from typing import Optional
from dataclasses import dataclass

@dataclass
class Disciplina:

    id_disciplina: Optional[int] = None
    nome: str
    carga_horaria: int
    semestre: str