file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')

file.seek(0, 0)
print('lendo linhas')
print(file.read())

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0, 0)
print(file.readlines())

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()
