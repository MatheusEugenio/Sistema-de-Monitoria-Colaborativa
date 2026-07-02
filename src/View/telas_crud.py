from View.base_crud import BaseCRUDFrame

class TelaUsuario(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(parent, "Usuário", ["Nome", "E-mail"], ["ID", "Nome", "E-mail"])

class TelaAluno(BaseCRUDFrame):
    def __init__(self, parent):
        super().__init__(parent, "Aluno", ["Matrícula", "CPF", "Curso", "ID Usuário"], ["ID", "Matrícula", "CPF", "Curso", "Nome"])