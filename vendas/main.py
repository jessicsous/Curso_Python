import vendas.calcula_preco
import vendas.formata.preco as formata

preco = 49.90
preco_com_aumento = vendas.calcula_preco.aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = vendas.calcula_preco.reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)

print(formata.real(50))