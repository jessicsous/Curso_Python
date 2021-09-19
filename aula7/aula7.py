nome = 'jessica silva'
idade = 23
altura = 1.50
e_maior = idade > 18
peso  = 50
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{0} tem {0} anos de idade e seu imc é {2}'.format(nome, idade, imc))  # colocar a numeração é importante pro caso de querer repetir uma variável
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
