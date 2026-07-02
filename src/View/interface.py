import customtkinter as ctk
from tkinter import ttk
from database.connection import get_connection

from View.telas_crud import TelaUsuario, TelaAluno, TelaProfessor, TelaDisciplina, TelaMonitor, TelaSessao

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class SistemaMonitoria(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Monitoria Colaborativa")
        self.geometry("1100x700")
        self.minsize(900, 600)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- MENU LATERAL ---
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#1a1a1a")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(8, weight=1)

        ctk.CTkLabel(self.sidebar, text="📌 Monitoria", font=ctk.CTkFont(size=24, weight="bold")).grid(row=0, column=0, padx=20, pady=(30, 20))

        self.telas = {}
        self.botoes = {}

        opcoes_menu = [
            ("Início", "Início"),
            ("Usuário", "Usuários"),
            ("Aluno", "Alunos"),
            ("Professor", "Professores"),
            ("Disciplina", "Disciplinas"),
            ("Monitor", "Monitores"),
            ("Sessão", "Sessões")
        ]

        for i, (id_tela, texto_botao) in enumerate(opcoes_menu):
            btn = ctk.CTkButton(
                self.sidebar, text=texto_botao, height=40, anchor="w",
                fg_color="transparent", hover_color="#2b2b2b",
                command=lambda t=id_tela: self.abrir_tela(t)
            )
            btn.grid(row=i+1, column=0, padx=10, pady=5, sticky="ew")
            self.botoes[id_tela] = btn

        self.frame_conteudo = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_conteudo.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.frame_conteudo.grid_rowconfigure(0, weight=1)
        self.frame_conteudo.grid_columnconfigure(0, weight=1)

        self.estilizar_tabelas()

        self.telas["Início"] = self.criar_tela_inicio()
        self.telas["Usuário"] = TelaUsuario(self.frame_conteudo)
        self.telas["Aluno"] = TelaAluno(self.frame_conteudo)
        self.telas["Professor"] = TelaProfessor(self.frame_conteudo)
        self.telas["Disciplina"] = TelaDisciplina(self.frame_conteudo)
        self.telas["Monitor"] = TelaMonitor(self.frame_conteudo)
        self.telas["Sessão"] = TelaSessao(self.frame_conteudo)

        self.abrir_tela("Início")