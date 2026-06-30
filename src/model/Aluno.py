from typing import Optional
from dataclasses import dataclass

@dataclass
class Aluno:

    id_aluno: Optional[int] = None 
    matricula: str
    cpf: str
    nome_curso: str
    #id_usuario: Optional[int] = None
    