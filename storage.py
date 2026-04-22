import csv 
import os
from models import Transacao

def salvar_transacao(transacao):
    file_path = "data/data.csv"
    entrada = [
                transacao.id,
                transacao.data,
                transacao.tipo,
                transacao.descricao,
                transacao.categoria,
                transacao.fonte,
                transacao.valor
            ]
    
    os.makedirs("data", exist_ok=True)

    if os.path.exists(file_path): 
        with open("data/data.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(entrada)
    else:
        with open("data/data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id","data","tipo","descricao","categoria","fonte","valor"])
            writer.writerow(entrada)
