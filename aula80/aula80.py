'''
Random - números aleatórios
'''

import random
import string

# Gera um número inteiro entre entre A e B
inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um número de ponto flutuante entre A e B
flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante1 = random.random()

# seleciona aleatóriamente valores de uma lista
lista = ['jéssica', 'Rellison', 'Lucas', 'nikole', 'sousa', 'silva', 'livanaldo']
sorteio = random.choices(lista, k=2)

lista = ['jéssica', 'Rellison', 'Lucas', 'nikole', 'sousa']
sorteio = random.choice(lista)

lista1 = ['jéssica', 'Rellison', 'Lucas', 'nikole', 'sousa']
for i in range(1000):
    sorteio1 = random.sample(lista, 2)

# Embaralhar lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%¨&*,.;_-/'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)