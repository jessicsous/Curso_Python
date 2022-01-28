'''
- É uma lista de listas de números inteiros
- As listas internas tem o tamanho de 10 elementos
- As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício

Crie uma função que encontra o primeiro duplicado considerando o segundo número com duplicação.
   Requisitos:
       A ordem dos números duplicados é considerada a partir da segunda
       ocorrência do número, ou seja, o número duplicado.
       Exemplo: [1, 2, 3, ->3<-, 2, 1] 3 (retorne 3)
       Se não encontrar duplicados na lista, retorne -1
'''
l1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 9],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def epd(param_list):
    numero_ch = set()

    for numero in param_list:
        if numero in numero_ch:
            return numero
        numero_ch.add(numero)

    return -1

for l in l1:
    print(l, epd(l))