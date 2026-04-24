from storage import carregar_transacoes
import datetime as dt


def resumo_tipo(transacoes, mes, ano):
    dados = [row for row in transacoes if int(row.data.split("-")[0]) == ano and int(row.data.split("-")[1]) == mes]
    resumo = {}
    for item in dados:
        resumo[item.tipo] = resumo.get(item.tipo, 0.0) + item.valor

    return resumo


def resumo_categoria(transacoes, mes, ano):
    dados = [row for row in transacoes if int(row.data.split("-")[0]) == ano and int(row.data.split("-")[1]) == mes]
    resumo = {}
    for item in dados:
        if item.tipo not in resumo:
            resumo[item.tipo] = {}
        resumo[item.tipo][item.categoria] = resumo[item.tipo].get(item.categoria, 0.0) + item.valor

    totais = resumo_tipo(transacoes, mes, ano)

    for tipo in resumo:
        total_tipo = totais[tipo]
        for categoria in resumo[tipo]:
            valor = resumo[tipo][categoria]
            percentual = (valor / total_tipo) * 100
            resumo[tipo][categoria] = {
                "valor": valor,
                "percentual": round(percentual, 1)
            }

    return resumo


def resumo_anual(transacoes, ano):
    hoje = dt.date.today()
    ultimo_mes = hoje.month if ano == hoje.year else 12
    
    resumo = {}
    for mes in range(1, ultimo_mes + 1):
        resumo[mes] = resumo_tipo(transacoes, mes, ano)
    return resumo


def relatorio_investimento_mensal(transacoes, mes, ano):
    totais = resumo_tipo(transacoes, mes, ano)
    salario_rows = [row for row in transacoes 
                if row.categoria == "salario" 
                and int(row.data.split("-")[0]) == ano 
                and int(row.data.split("-")[1]) == mes]

    
    entrada_salario = sum(row.valor for row in salario_rows)
    entrada = totais.get("entrada", 0.0)
    investimento = totais.get("investimento", 0.0)
    
    percentual_salario = (investimento / entrada_salario * 100) if entrada_salario > 0 else 0.0
    percentual = (investimento / entrada * 100) if entrada > 0 else 0.0
    
    return {
        "entrada_total": entrada,
        "salario": entrada_salario,
        "investimento": investimento,
        "percentual_total": round(percentual, 1),
        "percentual_salario": round(percentual_salario, 1)
    }
        

def relatorio_investimento_anual(transacoes, ano):
    totais = resumo_anual(transacoes, ano)
    base = {"entrada_total": 0, "investimento": 0, "percentual_total": 0}
    for mes in totais:
        base["entrada_total"] = base["entrada_total"] + totais[mes].get("entrada", 0.0)
        base["investimento"] = base["investimento"] + totais[mes].get("investimento", 0.0)

    base["percentual_total"] = round(base["investimento"] / base["entrada_total"] * 100,1) if base["entrada_total"] > 0 else 0.0

    return base