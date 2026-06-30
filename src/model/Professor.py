from typing import Optional
from dataclasses import dataclass

@dataclass
class Professor:

    id_professor: Optional[int] = None
    departamento: str
    #usuario_id: Optional[int] = None