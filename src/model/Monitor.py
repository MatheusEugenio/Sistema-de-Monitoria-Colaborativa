from typing import Optional
from dataclasses import dataclass

@dataclass
class Monitor:

    id_monitor: Optional[int] = None
    departamento: str
    #usuario_id: Optional[int] = None