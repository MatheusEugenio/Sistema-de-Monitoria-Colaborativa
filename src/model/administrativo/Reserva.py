from typing import Optional, List
from dataclasses import dataclass
from datetime import date
import psygopg2.extras
from database.connection import get_connection

enum StatusReserva:
    RESERVADO = "reservado"
    LIVRE = "livre"
    EM_USO = "em_uso"

@dataclass
class Reserva:

    id_reserva: Optional[int] = None
    data_reserva: datetime
    status: StatusReserva
   
class ReservaRepository:

    def reservaExiste(self, id_reserva: int, data_reserva: datetime) -> bool:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT * FROM reserva WHERE id_reserva = %s AND data_reserva = %s", (id_reserva, data_reserva))

            linha = cursor.fetchone()

            return linha is not None

        finally:
            cursor.close()
            connect.close()

    def buscarPorIdReserva(self, id_reserva: int) -> Optional[Reserva]:
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT * FROM reserva WHERE id_reserva = %s", (id_reserva,))

            linha = cursor.fetchone()

            return Reserva(**linha) if linha else None

        finally:
            cursor.close()
            connect.close()
            
    def listar(self) -> List[Reserva]:
        
        connect = get_connection()

        try:
            cursor = connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("SELECT id_reserva, data_reserva, status FROM reserva")

            linhas = cursor.fetchall()

            cursor.close()


            return [
                Reserva(
                    id_reserva=l["id_reserva"],
                    data_reserva=l["data_reserva"],
                    status=l["status"]
                ) for l in linhas
            ]

        finally:
            connect.close()

    def inserir(self, reserva: Reserva) -> None:
        
        connect = get_connection()

        try:
            cursor = connect.cursor()
            
            if self.reservaExiste(reserva.id_reserva, reserva.data_reserva):
                raise ValueError(f"Reserva com ID {reserva.id_reserva} e data {reserva.data_reserva} já existe.")
            try:
                cursor.execute(
                    """INSERT INTO reserva (data_reserva, status) 
                       VALUES (%s, %s)""",
                    (reserva.data_reserva, reserva.status),
                )

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

    def deletar(self, id_reserva: int) -> None:

        connect = get_connection()

        try:
            cursor = connect.cursor()

            try:
                cursor.execute("DELETE FROM reserva WHERE id_reserva = %s", (id_reserva,))

                connect.commit()

            except Exception:
                connect.rollback()
                raise

            finally:
                cursor.close()

        finally:
            connect.close()

