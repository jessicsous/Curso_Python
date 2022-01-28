string = '012345678901234567890123456789'
n = 10
contadores = [i for i in range(0, len(string), n)]
tupla = [(i, i + n) for i in range(0, len(string), n)]
lista = [string[i:i +n] for i in range(0, len(string), n)]
raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(contadores)
print(tupla)
print(raw)
print(lista)
print(retorno)