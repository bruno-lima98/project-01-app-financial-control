from storage import carregar_transacoes


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


file = "data.csv"
transacoes = carregar_transacoes(file)