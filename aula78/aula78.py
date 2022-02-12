"""
JavaScript object Notation - JSON
JSON (JavaScript object Notation) é um formato de troca de dados entre sistemas
e programas, muito leve e de fácil utilização. Muito utilizado por APIs
"""
from dados import *
import json

#lista = [1, 2, 3, 4, 5, 6]
#dados_json = json.dumps(lista)
#print(type(dados_json))

#dados_json1 = json.dumps(clientes_dicionario, indent = 4)
#print(dados_json1)

#dicionario = json.loads(clientes_json)

#for chave, valor in dicionario.items():
    #print(chave)
    #print(valor)

#with open('clientes.json', 'w') as arquivo:
    #json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)
