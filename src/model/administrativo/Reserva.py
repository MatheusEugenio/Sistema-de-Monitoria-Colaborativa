from typing import Optional, List
from dataclasses import dataclass
from datetime import date
from enum import Enum

from sqlalchemy import text
from database.connection import get_session

class StatusReserva(Enum):

    RESERVADO = "reservado"
    LIVRE = "livre"
    EM_USO = "em_uso"

@dataclass
class Reserva:

    id_reserva: Optional[int] = None
    data_reserva: datetime
    status: StatusReserva

class ReservaRepository:

    def reservaExiste(self,id_reserva: int,data_reserva: datetime) -> bool:

        session = get_session()

        try:

            resultado = session.execute(text("SELECT COUNT(*) FROM reserva WHERE id_reserva = :id AND data_reserva = :data"),{"id": id_reserva,"data": data_reserva})

            return resultado.scalar() > 0

        finally:
            session.close()


    def buscarPorIdReserva(self,id_reserva: int) -> Optional[Reserva]:

        session = get_session()

        try:

            resultado = session.execute(text("SELECT id_reserva, data_reserva, status FROM reserva WHERE id_reserva = :id"),{"id": id_reserva})

            linha = resultado.mappings().first()

            return Reserva(**linha) if linha else None

        finally:
            session.close()


    def listar(self) -> List[Reserva]:

        session = get_session()

        try:

            resultado = session.execute(text("SELECT id_reserva, data_reserva, status FROM reserva ORDER BY id_reserva"))

            linhas = resultado.mappings().all()

            return [Reserva(**linha) for linha in linhas]

        finally:
            session.close()


    def inserir(self, reserva: Reserva) -> None:

        session = get_session()

        try:

            if (reserva.id_reserva is not None and self.reservaExiste(reserva.id_reserva, reserva.data_reserva)):
                raise ValueError("Reserva já cadastrada.")

            session.execute(text("INSERT INTO reserva (data_reserva, status) VALUES (:data_reserva, :status)"),{"data_reserva": reserva.data_reserva, "status": reserva.status.value})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


    def deletar(self,id_reserva: int) -> None:

        session = get_session()

        try:

            session.execute(text("DELETE FROM reserva WHERE id_reserva = :id"),{"id": id_reserva})

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()