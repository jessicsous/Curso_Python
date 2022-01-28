from vendas.formata import preco

def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    return r

    if formata:
        return preco.real(r)
    else:
        return r

def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    return r

    if formata:
        return preco.real(r)
    else:
        return r