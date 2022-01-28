'''
comportamento de geradores
'''

# lista, tupla, str, sequences, iterável
nome = 'Jessica Sousa'

for letra in nome:
    print(letra)

print('#' * 80)

for letra in nome:
    print(letra)
print('#'* 80)

# o comportamento dos geradores e iteradores é diferente
iterador = iter(nome)

# try suprime o erro
try:
    print(next(iterador))  # j
    print(next(iterador))  # e
    print(next(iterador))  # s
    print(next(iterador))  # s
    print(next(iterador))  # i
    print(next(iterador))  # c
    print(next(iterador))  # a
    print(next(iterador))  #
    print(next(iterador))  # s
    print(next(iterador))  # o
    print(next(iterador))  # u
    print(next(iterador))  # s
    print(next(iterador))  # a
except:
    pass

for valor in iterador:  # não aparece porque o iterador inteiro ja foi consumido
    print(valor)


gerador = [letra for letra in nome]
gerador = iter(nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

for letra in gerador:  # vai terminar de consumir o resto do gerador
    print(letra)