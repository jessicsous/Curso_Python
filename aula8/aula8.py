'''
* criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* criar variável com o ano atual (int)
* obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
* obter o ano de nascimento da pessoa (baseando na idade e no ano atual)
* exibir um texto com todos os valores na tela usando f-string (com as chaves)
'''

nome = 'jessica silva de sousa'
altura = 1.50
peso = 50
idade = 23.9
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade, nasceu em {ano_nascimento:.0f} e seu imc é {imc:.2f}')



