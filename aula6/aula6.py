'''
iniciar com letra, pode conter números, separar _, letras minúsculas
'''

nome = 'jessica'  # variável 'nome', salvando esse valor na memória (apelido). não pode iniciar variável com numero
print(nome)  # a variável não precisa está dentro de aspas
print(nome, type(nome))  # a função type volta o valor da variável, nesse caso é uma 'str'

nome = 'jessica silva'
idade = 23  # int
altura = 1.50  # bool
e_maior = idade > 18  # a variável está sustentando a expressão, vai retornar um valor 'bool'
peso = 50
imc = peso * altura  # conta com variável é fora dos parenteses

print(nome, 'tem', idade, 'anos', 'e seu imc é', imc)

print()

print('nome', nome)
print('idade', idade)
print('altura', altura)
print('é maior:', e_maior)


print(idade * altura)  # é possível fazer conta com variáveis




