from dataclasses import dataclass
from typing import Optional

from sqlalhcemy import text
from database.connection import get_session

@dataclass
class Usuario:
    id_user: Optional[int] = None
    nome: str
    email: str

class UsuarioRepository:

    def buscarPorId(self, id_user: int) -> Optional[Usuario]:

        session = get_session()

        try:

            resultado = session.execute(text("SELECT id_user, nome, email FROM usuario WHERE id_user = :id"), {"id": id_user})

            linha = resultado.mappings().first()

            return Usuario(**linha) if linha else None

        finally:
            session.close()


    def existePorEmail(self, email: str) -> bool:

        session = get_session()

        try:

            resultado = session.execute(text("SELECT COUNT(*) FROM usuario WHERE email = :email"), {"email": email})

            return resultado.scalar() > 0

        finally:
            session.close()


    def listarUsuarios(self) -> List[Usuario]:

        session = get_session()

        try:

            resultado = session.execute(text("SELECT id_user, nome, email FROM usuario ORDER BY nome"))

            linhas = resultado.mappings().all()

            return [Usuario(**linha) for linha in linhas]

        finally:
            session.close()


    def inserir(self, usuario: Usuario) -> int:

        session = get_session()

        try:

            resultado = session.execute(text("INSERT INTO usuario (nome, email) VALUES (:nome, :email) RETURNING id_user"), {"nome": usuario.nome, "email": usuario.email})

            novo_id = resultado.scalar()

            session.commit()

            return novo_id

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


    def deletar(self, id_user: int) -> None:

        session = get_session()

        try:

            session.execute(text("DELETE FROM usuario WHERE id_user = :id"), {"id": id_user})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

 