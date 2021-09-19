'''
+ soma
- subtração
* multiplicação
/ divisão
// divisão inteira
** exponenciação
% resto da divisão
() parenteses - alterar a precedência nas contas
'''

print('adição', 10 + 10)
print('subtração', 10 - 10)
print('multiplicação', 10 * 10)
print('divisão', 10 / 10)
print('divisão inteira', 20.5 // 5)
print('elevação', 10 ** 2)
print('resto da divisão', 10 % 3)
print(5+2*10)
print((5+2)*10)  # uso do parentêses pra alterar a precedência

print('')

# comportamentos diferentes dos operadores
print(10 * '10')  # o operador de multiplicação também serve como operador de repetição
print(10 * 'a')
print('5' + '5')  # conatenação
print('jessica' + ' ' + 'silva')  # concatenação
print('jessica' + ' ' + 'silva' + ' ' + str(23) + ' ' + 'anos')  # concatenação e tranformação de inteiro em string


