from View.base_crud import BaseCRUDFrame

class TelaUsuario(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(parent, "Usuário", ["Nome", "E-mail"], ["ID", "Nome", "E-mail"])

class TelaAluno(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(parent, "Aluno", ["Matrícula", "CPF", "Curso", "ID Usuário"], ["ID", "Matrícula", "CPF", "Curso", "Nome"])
        
class TelaProfessor(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(parent, "Professor", ["Departamento", "ID Usuário"], ["ID", "Departamento", "Nome"])

class TelaDisciplina(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(parent, "Disciplina", ["Nome", "Carga Horária", "Semestre"], ["ID", "Nome", "CH", "Semestre"])

class TelaMonitor(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(parent, "Monitor", ["Departamento", "ID Aluno"], ["ID", "Departamento", "Nome"])

class TelaSessao(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(
            parent, 
            "Sessão", 
            ["Data", "Horário", "Limite Part.", "ID Monitoria", "Descrição"], 
            ["ID", "Data", "Horário", "Limite Part.", "Monitor", "Descrição"]
        )