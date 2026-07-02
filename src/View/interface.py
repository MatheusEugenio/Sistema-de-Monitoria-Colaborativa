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

    def abrir_tela(self, id_tela):
        """Esconde a tela anterior, destaca o botão selecionado e atualiza se for o Dashboard."""
        for tela in self.telas.values():
            tela.grid_forget()
        for btn in self.botoes.values():
            btn.configure(fg_color="transparent")

        self.telas[id_tela].grid(row=0, column=0, sticky="nsew")
        self.botoes[id_tela].configure(fg_color="#2b2b2b")

       
        if id_tela == "Início":
            self.atualizar_dashboard()

    def criar_tela_inicio(self):
        frame = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        ctk.CTkLabel(frame, text="Dashboard Geral", font=ctk.CTkFont(size=28, weight="bold")).pack(anchor="w", pady=(0, 20))

        grid_cards = ctk.CTkFrame(frame, fg_color="transparent")
        grid_cards.pack(fill="x", pady=10)

        def criar_card(parent, titulo, cor):
            card = ctk.CTkFrame(parent, fg_color=cor, corner_radius=10, height=100, width=200)
            card.pack(side="left", padx=10, expand=True, fill="both")
            card.pack_propagate(False)
            ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=14, weight="bold"), text_color="white").pack(pady=(15, 5))

            lbl_valor = ctk.CTkLabel(card, text="...", font=ctk.CTkFont(size=32, weight="bold"), text_color="white")
            lbl_valor.pack()
            return lbl_valor

        self.lbl_val_alunos = criar_card(grid_cards, "Alunos Ativos", "#1f538d")
        self.lbl_val_monitores = criar_card(grid_cards, "Monitores", "#2b8a3e")
        self.lbl_val_sessoes = criar_card(grid_cards, "Sessões Hoje", "#c92a2a")
        self.lbl_val_disciplinas = criar_card(grid_cards, "Disciplinas", "#e67700")

        ctk.CTkLabel(frame, text="Bem-vindo ao Sistema de Monitoria Colaborativa!\nSelecione um módulo no menu lateral para iniciar o gerenciamento.",
                    font=ctk.CTkFont(size=16), text_color="gray").pack(pady=40)

        ctk.CTkButton(frame, text="🔄 Atualizar Dashboard", command=self.atualizar_dashboard, fg_color="#242424", hover_color="#2b2b2b").pack()

        return frame

    def atualizar_dashboard(self):
        if not hasattr(self, 'lbl_val_alunos'):
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM aluno;")
            self.lbl_val_alunos.configure(text=str(cursor.fetchone()[0]))

            cursor.execute("SELECT COUNT(*) FROM monitor;")
            self.lbl_val_monitores.configure(text=str(cursor.fetchone()[0]))

            cursor.execute("SELECT COUNT(*) FROM sessao WHERE data = CURRENT_DATE;")
            self.lbl_val_sessoes.configure(text=str(cursor.fetchone()[0]))

            cursor.execute("SELECT COUNT(*) FROM disciplina;")
            self.lbl_val_disciplinas.configure(text=str(cursor.fetchone()[0]))

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao recarregar dados do dashboard: {e}")
            for lbl in [self.lbl_val_alunos, self.lbl_val_monitores, self.lbl_val_sessoes, self.lbl_val_disciplinas]:
                if lbl.winfo_exists():
                    lbl.configure(text="Erro")

    def estilizar_tabelas(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2b2b2b", foreground="white", rowheight=30, fieldbackground="#2b2b2b", borderwidth=0)
        style.map('Treeview', background=[('selected', '#1f538d')])
        style.configure("Treeview.Heading", background="#1a1a1a", foreground="white", relief="flat", font=('Arial', 10, 'bold'))