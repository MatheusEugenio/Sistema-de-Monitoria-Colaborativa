import customtkinter as ctk
from tkinter import ttk, messagebox
import unicodedata
from database.connection import get_connection

class BaseCRUDFrame(ctk.CTkFrame):
    def __init__(self, parent, nome, campos, colunas):
        super().__init__(parent, fg_color="transparent")
        self.nome = nome  
        self.campos = campos  
        self.colunas = colunas  
        
        tabelas_db = {
            "Usuário": "usuario",
            "Aluno": "aluno",
            "Professor": "professor",
            "Disciplina": "disciplina",
            "Monitor": "monitor",
            "Sessão": "sessao"
        }
        self.tabela = tabelas_db.get(self.nome, self.nome.lower())
        
        self.inputs = {}
        self.configurar_interface()
        self.carregar_dados()

    def configurar_interface(self):
        titulos_plural = {
            "Usuário": "Usuários", "Aluno": "Alunos", "Professor": "Professores",
            "Disciplina": "Disciplinas", "Monitor": "Monitores", "Sessão": "Sessões"
        }
        nome_correto = titulos_plural.get(self.nome, self.nome + "s")

        ctk.CTkLabel(self, text=f"Gerenciar {nome_correto}", font=ctk.CTkFont(size=24, weight="bold")).pack(anchor="w", pady=(0, 20))

        card_form = ctk.CTkFrame(self, fg_color="#242424", corner_radius=15)
        card_form.pack(fill="x", pady=(0, 20), ipady=15)

        grid_inputs = ctk.CTkFrame(card_form, fg_color="transparent")
        grid_inputs.pack(fill="x", padx=20, pady=15)

        for i, campo in enumerate(self.campos):
            grid_inputs.grid_columnconfigure(i, weight=1)
            box = ctk.CTkFrame(grid_inputs, fg_color="transparent")
            box.grid(row=0, column=i, padx=10, sticky="ew")
            
            ctk.CTkLabel(box, text=campo, font=ctk.CTkFont(size=12)).pack(anchor="w", padx=2)
            entry = ctk.CTkEntry(box, placeholder_text=f"{campo}...", height=35)
            entry.pack(fill="x", pady=5)
            self.inputs[campo] = entry

        box_botoes = ctk.CTkFrame(card_form, fg_color="transparent")
        box_botoes.pack(fill="x", padx=20, pady=(5, 10))

        btn_salvar = ctk.CTkButton(box_botoes, text="Salvar", fg_color="#2b8a3e", hover_color="#236d32", command=self.salvar)
        btn_salvar.pack(side="left", padx=5, expand=True, fill="x")

        btn_atualizar = ctk.CTkButton(box_botoes, text="🔄 Atualizar Registro", fg_color="#1f538d", hover_color="#163c66", command=self.atualizar_registro)
        btn_atualizar.pack(side="left", padx=5, expand=True, fill="x")

        btn_excluir = ctk.CTkButton(box_botoes, text="Excluir", fg_color="#c92a2a", hover_color="#9c2020", command=self.excluir)
        btn_excluir.pack(side="left", padx=5, expand=True, fill="x")

        btn_carregar = ctk.CTkButton(box_botoes, text="Carregar Dados", fg_color="#495057", hover_color="#343a40", command=self.carregar_dados)
        btn_carregar.pack(side="left", padx=5, expand=True, fill="x")

        self.tree = ttk.Treeview(self, columns=self.colunas, show="headings")
        
        for col in self.colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
            
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_linha_selecionada)

    def _normalizar_nome_coluna(self, campo):
        s = campo.lower().replace(".", "").replace("-", "").replace(" ", "_")
        s = "".join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
        
        mapa_colunas = {
            "id": "id_user" if self.tabela == "usuario" else f"id_{self.tabela}",
            "id_usuario": "id_usuario",
            "id_user": "id_user",
            "limite_part": "limite_participantes",
            "limite_participantes": "limite_participantes",
            "ch": "carga_horaria",
            "carga_horaria": "carga_horaria",
            "monitor": "id_monitoria",
            "id_monitoria": "id_monitoria",
            "id_aluno": "id_aluno",
            "id_professor": "id_professor",
            "nome": "nome",
            "curso": "nome_curso" 
        }
        return mapa_colunas.get(s, s)
    def carregar_dados(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        coluna_id = "id_user" if self.tabela == "usuario" else f"id_{self.tabela}"
            
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if self.tabela == "aluno":
                query = f"SELECT a.*, u.nome, a.id_usuario FROM aluno a INNER JOIN usuario u ON a.id_usuario = u.id_user ORDER BY a.{coluna_id} ASC;"
            elif self.tabela == "professor":
                query = f"SELECT p.*, u.nome, p.id_professor AS id_usuario FROM professor p INNER JOIN usuario u ON p.id_professor = u.id_user ORDER BY p.{coluna_id} ASC;"
            elif self.tabela == "monitor":
                query = f"SELECT m.*, u.nome, m.id_aluno FROM monitor m INNER JOIN aluno a ON m.id_aluno = a.id_aluno INNER JOIN usuario u ON a.id_usuario = u.id_user ORDER BY m.{coluna_id} ASC;"
            else:
                query = f"SELECT * FROM {self.tabela} ORDER BY {coluna_id} ASC;"
                
            cursor.execute(query)
            colunas_db = [desc[0] for desc in cursor.description]
            linhas = cursor.fetchall()
            
            for linha in linhas:
                row_dict = dict(zip(colunas_db, linha))
                tree_values = []
                
                for col_visual in self.colunas:
                    col_db = self._normalizar_nome_coluna(col_visual)
                    tree_values.append(row_dict.get(col_db, ""))
                    
                self.tree.insert("", "end", values=tree_values)
                
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao carregar dados de {self.tabela}: {e}")

def on_linha_selecionada(self, event):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            return
            
        valores_tree = self.tree.item(item_selecionado, "values")
        id_registro = valores_tree[0]  
        coluna_id = "id_user" if self.tabela == "usuario" else f"id_{self.tabela}"
        
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            # Garantimos que a linha específica também puxa os IDs explícitos e aliases
            if self.tabela == "aluno":
                query = f"SELECT a.*, u.nome, a.id_usuario FROM aluno a INNER JOIN usuario u ON a.id_usuario = u.id_user WHERE a.{coluna_id} = %s;"
            elif self.tabela == "professor":
                query = f"SELECT p.*, u.nome, p.id_professor AS id_usuario FROM professor p INNER JOIN usuario u ON p.id_professor = u.id_user WHERE p.{coluna_id} = %s;"
            elif self.tabela == "monitor":
                query = f"SELECT m.*, u.nome, m.id_aluno FROM monitor m INNER JOIN aluno a ON m.id_aluno = a.id_aluno INNER JOIN usuario u ON a.id_usuario = u.id_user WHERE m.{coluna_id} = %s;"
            else:
                query = f"SELECT * FROM {self.tabela} WHERE {coluna_id} = %s;"
                
            cursor.execute(query, (id_registro,))
            linha = cursor.fetchone()
            
            if linha:
                colunas_db = [desc[0] for desc in cursor.description]
                row_dict = dict(zip(colunas_db, linha))
                
                for campo, entry in self.inputs.items():
                    col_db = self._normalizar_nome_coluna(campo)
                    entry.delete(0, "end")
                    if col_db in row_dict and row_dict[col_db] is not None:
                        entry.insert(0, str(row_dict[col_db]))
                        
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao selecionar linha: {e}")

def salvar(self):
        valores = []
        colunas_db = []
        coluna_id = "id_user" if self.tabela == "usuario" else f"id_{self.tabela}"
        
        for campo, entry in self.inputs.items():
            col_db = self._normalizar_nome_coluna(campo)
            
            if col_db == "nome" and self.tabela in ["aluno", "professor", "monitor"]:
                continue
                
            if col_db == coluna_id:
                continue  
                
            valor = entry.get().strip()
            if not valor:
                messagebox.showwarning("Aviso", f"O campo '{campo}' não pode estar vazio.")
                return
            
            valores.append(valor)
            colunas_db.append(col_db)
            
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            colunas_str = ", ".join(colunas_db)
            placeholders = ", ".join(["%s"] * len(valores))
            query = f"INSERT INTO {self.tabela} ({colunas_str}) VALUES ({placeholders});"
            
            cursor.execute(query, tuple(valores))
            conn.commit()
            cursor.close()
            conn.close()
            
            messagebox.showinfo("Sucesso", f"{self.nome} cadastrado com sucesso!")
            self.carregar_dados()
            
            for entry in self.inputs.values():
                entry.delete(0, "end")
        except Exception as e:
            messagebox.showerror("Erro ao Salvar", f"Erro:\n{e}")

def atualizar_registro(self):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione um registo na tabela para atualizar.")
            return
            
        valores_tree = self.tree.item(item_selecionado, "values")
        id_registro = valores_tree[0]
        coluna_id = "id_user" if self.tabela == "usuario" else f"id_{self.tabela}"
            
        set_statements = []
        valores = []
        
        for campo, entry in self.inputs.items():
            col_db = self._normalizar_nome_coluna(campo)
            
            if col_db == coluna_id or col_db == "id_user" or col_db.startswith("id_"):
                continue 
                
            if col_db == "nome" and self.tabela in ["aluno", "professor", "monitor"]:
                continue
                
            valor = entry.get().strip()
            if not valor:
                messagebox.showwarning("Aviso", f"O campo '{campo}' não pode estar vazio.")
                return
                
            set_statements.append(f"{col_db} = %s")
            valores.append(valor)
            
        if not set_statements:
            messagebox.showinfo("Informação", "Nenhum campo editável foi alterado (IDs não podem ser modificados).")
            return
            
        valores.append(id_registro)  
        
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            set_str = ", ".join(set_statements)
            query = f"UPDATE {self.tabela} SET {set_str} WHERE {coluna_id} = %s;"
            
            cursor.execute(query, tuple(valores))
            conn.commit()
            cursor.close()
            conn.close()
            
            messagebox.showinfo("Sucesso", f"{self.nome} atualizado com sucesso!")
            self.carregar_dados()
            
            for entry in self.inputs.values():
                entry.delete(0, "end")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao atualizar:\n{e}")

def excluir(self):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione um registo para excluir.")
            return

        valores = self.tree.item(item_selecionado, "values")
        id_registro = valores[0]
        coluna_id = "id_user" if self.tabela == "usuario" else f"id_{self.tabela}"

        if messagebox.askyesno("Confirmar", f"Deseja excluir o registo {id_registro}?"):
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM {self.tabela} WHERE {coluna_id} = %s;", (id_registro,))
                conn.commit()
                cursor.close()
                conn.close()
                
                messagebox.showinfo("Sucesso", "Excluído com sucesso!")
                self.carregar_dados()
                for entry in self.inputs.values():
                    entry.delete(0, "end")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao excluir (Verifique Vínculos):\n{e}")
