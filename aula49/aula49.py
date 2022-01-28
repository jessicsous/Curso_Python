# https://docs.python.org/3/library/functions.html#open

file = open('abc.txt', 'w+') # criou um arquivo  zerou ele
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')

file.seek(0, 0)  # colocou o cursor no inicio do arquivo
print('lendo linhas:')
print(file.read())  # leu oqq tinha no arquivo
print('############')

file.seek(0, 0)  # voltou pro começo
print(file.readline(), end='')  # leu linha por linha
print(file.readline(), end='')
print(file.readline(), end='')
print('############')
file.seek(0, 0)
#print(file.readlines())  #cria uma lista
for linha in file.readlines():
    print(linha)

file.close()