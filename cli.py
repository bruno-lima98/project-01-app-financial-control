import re
from datetime import datetime

def menu_inicial():
    print(" CONSOLE FINANCEIRO v1.0 ".center(50, "="))
    print("""
[1] Acessar transações gerais
[2] Acessar estatísticas financeiras
[3] Registrar uma nova transação
[4] Editar transação (Atualizar/Deletar)
[5] Sair 
          """)
    while True:
        try:
            resposta = int(input("Selecione uma opção: ").strip())
        except ValueError:
            print("Valor inválido selecionado.")
        else:
            if resposta == 5:
                return print("Programa encerrado.")
            elif resposta in [1, 2, 3, 4]:
                if resposta == 1:
                    return listar_transacoes()
                elif resposta == 2:
                    return menu_estatistica()
                elif resposta == 3:
                    return registrar_transacao()
                else:
                    return menu_edicao()
            else:
                print("Opção não encontrada.")
                continue
    

def menu_estatistica():
    print(" 2. ESTATÍSTICAS FINACEIRAS ".center(50, "="))
    print("""
[1] Resumo por tipo de transação
[2] Resumo por categoria de transações
[3] Resumo anual geral
[4] Relatório de investimento mensal
[5] Relatório de investimento anual 
[6] Retornar
[7] Sair
          """)
    while True:
        try:
            resposta = int(input("Selecione uma opção: ").strip())
        except ValueError:
            print("Valor inválido selecionado.")
        else:
            if resposta == 7:
                return print("Programa encerrado.")
            elif resposta == 6:
                return menu_inicial()
            elif resposta in [1, 2, 3, 4, 5]:
                return print("teste")
            else:
                print("Opção não encontrada.")
                continue


def menu_edicao():
    print(" 4. EDIÇÃO DE TRANSAÇÕES ".center(50, "="))
    print("""
[1] Atualizar transação
[2] Deletar transação
[3] Retornar
[4] Sair 
          """)
    while True:
        try:
            resposta = int(input("Selecione uma opção: ").strip())
        except ValueError:
            print("Valor inválido selecionado.")
        else:
            if resposta == 4:
                return print("Programa encerrado.")
            elif resposta == 3:
                return menu_inicial()
            elif resposta in [1, 2]:
                return print("teste")
            else:
                print("Opção não encontrada.")
                continue

def listar_transacoes():
    pass

def registrar_transacao():
    
    ## Validação da data:
    print(" 3.1. DATA ".center(50, "="))
    while True:
       data = input("Data: ").strip()
       validar = validar_data(data)
       if validar == True:
           break
    print()

    ## Validação de tipo:
    print(" 3.2. TIPO ".center(50, "="))
    print("""[1] Entrada
[2] Saída
[3] Investimento
[4] Investimento Internacional
[5] Reserva IN
[6] Reserva OUT
          """)
    while True:
        try:
            tipo = int(input("Tipo: ").strip())
        except ValueError:
            print("Formato inválido de entrada.")
        else:
            validar, tipo = validar_tipo(tipo)
            if validar == True:
                break
    print()


    return print(data, tipo)


def validar_data(data):
    padrao_barra = r"^\d{2}/\d{2}/(?:\d{2}|\d{4})$"
    meses = {
        "01": 31,
        "02": 28,
        "03": 31,
        "04": 30,
        "05": 31,
        "06": 30,
        "07": 31,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31
    }

    if re.match(padrao_barra, data): # Validação do padrão de entrada
        dia, mes, ano = data.split("/")

        # Validando ano bissexto:
        if int(ano) % 400 == 0 or (int(ano) % 4 == 0 and int(ano) % 100 != 0):
            meses["02"] = 29

        pendencias = {"dia": "válido", "mes": "válido", "ano": "válido"}
        try:
            if int(dia) < 1 or int(dia) > meses[mes]:
                pendencias["dia"] = "inválido"
        except KeyError:
            pendencias["mes"] = "inválido"
        if int(mes) < 1 or int(mes) > 12:
            pendencias["mes"] = "inválido"
        if len(ano) == 4 and (int(ano) < 2020 or int(ano) > datetime.today().year):
            pendencias["ano"] = "inválido"
        if len(ano) == 2 and (int(ano) < 20 or int(ano) > int(str(datetime.today().year)[2:])):
            pendencias["ano"] = "inválido"

        i = 0 ## !! Utilizar if all() para simplificar << refatoração posterior
        for valor in pendencias.values():
            if valor == "válido":
                i += 1
        
        if i == 3:
            return True
        else:
            for item, valor in pendencias.items():
                if valor == "inválido":
                    print(f"{item.title()} fora do padrão.")
                else:
                    continue
            return False
    else:
        print("Data fora do padrão.")
        return False


def validar_tipo(tipo):
    tipos = {
        1: "Entrada",
        2: "Saída",
        3: "Investimento",
        4: "Investimento Internacional", 
        5: "Reserva IN",
        6: "Reserva OUT"       
        }
    
    if tipo in [1, 2, 3, 4, 5, 6]:
        return True, tipos[tipo]
    else:
        print("Opção inválida.")
        return False, None
