import pandas as pd

from models import Disponibilidade, DisponibilidadeRepository
import controllers.MonitorController as monitor_controller

repo = DisponibilidadeRepository()

DIAS_SEMANA = [
    "Segunda-feira", "Terça-feira", "Quarta-feira",
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo",
]

def listar():
    return repo.listar()


def listar_como_dataframe() -> pd.DataFrame:
    dados = repo.listar()
    if not dados:
        return pd.DataFrame(columns=["id_disponibilidade", "horario_inicio", "horario_final",
                                      "data_inicio", "data_fim", "dia_semana", "id_monitor"])
    return pd.DataFrame([d.__dict__ for d in dados])


def opcoes_monitores() -> dict:
    return monitor_controller.opcoes_monitores()


def opcoes_dias_semana() -> list:
    return DIAS_SEMANA

def cadastrar(horario_inicio: str, horario_final: str, data_inicio: str,
              data_fim: str, dia_semana: str, id_monitor: int):

    if not horario_inicio or not horario_final:
        return False, "Horários de início e fim são obrigatórios."
    if not data_inicio or not data_fim:
        return False, "Datas de início e fim são obrigatórias."
    if not dia_semana:
        return False, "Dia da semana é obrigatório."

    try:

        if repo.buscarPorData_hora(horario_inicio, horario_final, data_inicio, data_fim):
            return False, "Disponibilidade já cadastrada."

        repo.inserir(Disponibilidade(
            horario_inicio=horario_inicio,
            horario_final=horario_final,
            data_inicio=data_inicio,
            data_fim=data_fim,
            dia_semana=dia_semana,
            id_monitor=id_monitor,
        ))
        return True, "Disponibilidade cadastrada com sucesso."

    except Exception as erro:
        return False, f"Erro: {erro}"


def remover(id_disponibilidade: int):

    try:
        if not repo.buscarDisponibilidadePorId(id_disponibilidade):
            raise ValueError("Disponibilidade não encontrada.")

        repo.deletar(id_disponibilidade)
        return True, "Disponibilidade removida."
    except Exception as erro:
        return False, f"Erro: {erro}"