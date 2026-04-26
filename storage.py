import csv 
import os
from models import Transacao


# FUNÇÕES PRINCIPAIS DO APP:
# 1 - salvar_transacao: salva uma transação nova no banco de dados
# 2 - carregar_transacoes: retorna todas as transações salvas no banco de dados
# 3 - deletar_transacoes: seleciona uma transação (via uuid) e remove do banco de dados
# 4 - atualizar_transacoes: atualiza uma transação selecionada (via uuidd). É necessário passar a transação completa atualizada.

def salvar_transacao(transacao):
    # Local onde ficarão os arquivos:
    file_path = "data/data.csv"

    # Lista de entrada do objeto Transacao:
    entrada = _transacao_para_lista(transacao)
    
    # Criar a folder caso seja a primeira transação:
    os.makedirs("data", exist_ok=True)

    # Inserir e salvar a transação, verificando se é a primeira transação ou não:
    if os.path.exists(file_path): 
        with open("data/data.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(entrada)
    else:
        with open("data/data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id","data","tipo","descricao","categoria","fonte","valor"])
            writer.writerow(entrada)


def carregar_transacoes():
    file_path = f"data/data.csv"

    if os.path.exists(file_path): 
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader) # Armazena o cabeçalho e remove dos dados
            
            saida = []
            for row in reader:
                dic = dict(zip(header,row))
                saida.append(Transacao(**dic))
        
        return saida
    else:
        return []


def deletar_transacoes(id):
    file_path = "data/data.csv"

    if not os.path.exists(file_path):
        return print("Sem arquivo CSV.")
    else:
        dados_atual = carregar_transacoes("data.csv")
        saida = [row for row in dados_atual if row.id != id]
        salvar_todas(saida)


def atualizar_transacoes(id, transacao_nova):
    file_path = "data/data.csv"

    if not os.path.exists(file_path):
        return print("Sem arquivo CSV.")
    else:
        dados_atual = carregar_transacoes("data.csv")
        for i, row in enumerate(dados_atual):
            if row.id == id:
                dados_atual[i] = transacao_nova
            else:
                continue
        salvar_todas(dados_atual)


# FUNÇÕES AUXILIARES DO APP:
# 1 - salvar_todas: reescreve o banco de dados com dados atualizados
# 2 - _transacao_para_lista: converte uma Transação (objeto) para lista

def salvar_todas(transacoes):
    file_path = "data/data.csv" 
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id","data","tipo","descricao","categoria","fonte","valor"])
        for row in transacoes:
            writer.writerow(_transacao_para_lista(row))


def _transacao_para_lista(transacao):
    return [
        transacao.id,
        transacao.data,
        transacao.tipo,
        transacao.descricao,
        transacao.categoria,
        transacao.fonte,
        transacao.valor
        ]