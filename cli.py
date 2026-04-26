import re
from datetime import datetime
from models import Transacao
from storage import salvar_transacao, carregar_transacoes


def menu_inicial():
    print(" CONSOLE FINANCEIRO v1.0 ".center(80, "="))
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
                    return menu_transacoes()
                elif resposta == 2:
                    return menu_estatistica()
                elif resposta == 3:
                    return registrar_transacao()
                else:
                    return menu_edicao()
            else:
                print("Opção não encontrada.")
                continue


################### OPÇÃO 1: OPÇÕES DE VISUALIZAÇÃO DE TRANSAÇÕES ###################

def menu_transacoes():
    print(" 1. TRANSAÇÕES GERAIS".center(80, "="))
    print("""
[1] Exibir todas as transações
[2] Filtrar período de exibição
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
            elif resposta == 1:
                return listar_transacoes()
            elif resposta == 2:
                while True:
                    try:
                        mes, ano = input("Selecione o período (MM/AAAA): ").split("/")
                        return listar_transacoes(int(mes), int(ano))
                    except ValueError:
                        print("Data informada é inválida.")
            else:
                print("Opção não encontrada.")
                continue


def listar_transacoes(mes=None, ano=None):

    cabecalho = (f"{'n':^3} | {'Data':^10} | {'Tipo':^15} | {'Descrição':^25} | {'Categoria':^22} | {'Fonte':^10}  | {'Valor':^8}")
    print(cabecalho)
    print("-"*len(cabecalho))

    lista = sorted(carregar_transacoes(),  key=lambda x: x.data, reverse=True)
    if mes and ano:
        lista = [row for row in lista if datetime.fromisoformat(row.data).month == mes 
                 and datetime.fromisoformat(row.data).year == ano]

    i=1
    for row in lista:
        print(
            f"{i:>3} | {datetime.strptime(row.data, '%Y-%m-%d').strftime('%d/%m/%Y')} | {row.tipo:^15} | {row.descricao:<25} | "
            f"{row.categoria:^22} | {row.fonte:^10}  | R$ {row.valor:^8.2f}"
        )
        i += 1
    return
    

################## OPÇÃO 2: OPÇÕES DE VISUALIZAÇÃO DE ESTATÍSTICAS ##################

def menu_estatistica():
    print(" 2. ESTATÍSTICAS FINACEIRAS ".center(80, "="))
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


##################### OPÇÃO 3: OPÇÕES DE REGISTRO DE TRANSAÇÕES #####################

def registrar_transacao(): 
    ## !! Implementar limpeza de dados errados os.system para melhor UX << refatoração posterior
    
    ## Validação da data:
    print(" 3.1. DATA ".center(80, "="))
    print()
    while True:
       data = input("Data: ").strip()
       validar = validar_data(data)
       if validar == True:
           break
    print()

    ## Validação de tipo:
    print(" 3.2. TIPO ".center(80, "="))
    print("""
[1] Entrada
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

    ## Validação de categoria:
    print(" 3.3. DESCRIÇÃO ".center(80, "="))
    print()
    print("Descreva a sua transação.")
    descricao = input("Descrição: ").strip()
    print()

    ## Validação de categoria:
    print(" 3.4. CATEGORIA ".center(80, "="))
    print(f"""
{'[1] Salário':<24} {'[10] Ifood':<24} {'[19] Atividade Física':<24}
{'[2] Vale Refeição':<24} {'[11] Comida Fora':<24} {'[20] Lazer':<24}
{'[3] Vale Alimentação':<24} {'[12] Comida p/ Cozinhar':<24} {'[21] Suplementos':<24}
{'[4] Saldo Livre ':<24} {'[13] Compra Online':<24} {'[22] Dinheiro Jac':<24}
{'[5] Saldo Mobilidade':<24} {'[14] Compra Padrão':<24} {'[23] Investimento':<24}
{'[6] Aluguel':<24} {'[15] Farmácia':<24} {'[24] Investimento Internacional':<24}
{'[7] Mercado':<24} {'[16] Role':<24} {'[25] Reserva de Emergência':<24}
{'[8] Streaming':<24} {'[17] Transporte':<24} {'[26] Reserva Adicional':<24}
{'[9] Viagem':<24} {'[18] Uber':<24} {'[27] Outros':<24}
          """)
    while True:
        try:
            categoria = int(input("Categoria: ").strip())
        except ValueError:
            print("Formato inválido de entrada.")
        else:
            validar, categoria = validar_categoria(categoria)
            if validar == True:
                break
    print()

    ## Validação de fonte:
    print(" 3.5. FONTE DA TRANSAÇÃO ".center(80, "="))
    print("""
[1] Dinheiro
[2] Vale Refeição
[3] Vale Alimentação
[4] Saldo Livre
[5] Saldo Mobilidade
          """)
    while True:
        try:
            fonte = int(input("Tipo: ").strip())
        except ValueError:
            print("Formato inválido de entrada.")
        else:
            validar, fonte = validar_fonte(fonte)
            if validar == True:
                break
    print()

    ## Validação de fonte:
    print(" 3.6. VALOR DA TRANSAÇÃO ".center(80, "="))
    print()
    print("Especifique o valor da sua transação.")
    while True:
        try:
            valor = float(input("Valor (R$): ").strip())
        except ValueError:
            print("Formato inválido de entrada.")
        else:
            break
    print()

    salvar_transacao(Transacao(data, tipo, categoria, fonte, valor, descricao=descricao))
    print("Sua transação foi registrada no banco de dados.")
    print(f"{data} | {tipo} | {descricao} | {categoria} | {fonte} | {valor}")
    return


############### OPÇÃO 4: OPÇÕES DE ATUALIZAÇÃO/REMOÇÃO DE TRANSAÇÕES ################

def menu_edicao():
    print(" 4. EDIÇÃO DE TRANSAÇÕES ".center(80, "="))
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


################################# FUNÇÕES AUXILIARES ################################

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
        1: "entrada",
        2: "saida",
        3: "investimento",
        4: "investimento_internacional", 
        5: "reserva_in",
        6: "reserva_out"       
        }
    
    if tipo in tipos:
        return True, tipos[tipo]
    else:
        print("Opção inválida.")
        return False, None
    

def validar_categoria(categoria):
    categorias = {
        1: "salario", 10: "ifood", 19:"atividade_fisica",
        2: "vale_refeicao", 11: "comida_fora", 20:"lazer",
        3: "vale_alimentacao", 12: "comida_para_cozinhar", 21:"suplementos",
        4: "saldo_livre", 13: "compra_online", 22:"dinheiro_jac",
        5: "saldo_mobilidade", 14: "compra_padrao", 23:"investimento",
        6: "aluguel", 15: "farmacia", 24:"investimento_internacional",
        7: "mercado", 16: "role", 25:"reserva_de_emergencia",
        8: "streaming", 17: "transporte", 26:"reserva_adicional",
        9: "viagem", 18: "uber", 27:"outros",
    }
    if categoria in categorias:
        return True, categorias[categoria]
    else:
        print("Opção inválida.")
        return False, None
    

def validar_fonte(fonte):
    fontes = {
        1: "dinheiro",
        2: "vale_refeicao",
        3: "vale_alimentacao",
        4: "saldo_livre", 
        5: "saldo_mobilidade",      
        }
    
    if fonte in fontes:
        return True, fontes[fonte]
    else:
        print("Opção inválida.")
        return False, None