from dataclasses import dataclass
#from datetime import datetime
from database.connection import get_connection

@dataclass
class Usuario:
    id_aluno: Optional[int] = None
    nome: str
    email: str

class UsuarioRepository:
    
    def listarUsuarios(self, tipo: str = None) -> List[Usuario]:

        connect = get_connection()
        cursor = connect.cursor()

        cursor.execute("Select * from usuario")

        usuarios = cursor.fetchall()

        cursor.close()
        connection.close()

        return usuarios
           



 