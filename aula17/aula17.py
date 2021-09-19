'''
* manipulando strings
* fatiamento de strings
* funções podem ser usadas diretamente em cada tipo.

pode conferir tudo em:
https://docs.python.org/3/library.html (tipos built-in)
https://docs.python.org/3/library.html (funções built-in)
'''
# positivos  [012345678]
texto      = 'python s2'

print( texto [2])  # acessar o indíce
print( texto [8])
print( texto [6])

# indices negativos [876543210]
texto =             'python s2'

print( texto [8])
print( texto [4])
print( texto [2])

# eliminar a barra
url = 'www.google.com.br/'
texto0 = 'www.google.com.br/'
nova_string0 = texto0[-6:-2]
print( url[:-17] )
print(url[0::2])  # :: pular de 2 em 2 caracteres
print(nova_string0)

# fatiar string
texto = 'jessica'
nova_string = texto[2:6]  # 2: inicio, 6: fim. o caracter 6 ñ é incluído
nova_string1 = texto[5:]  # pegar do caracter 5 até o final
print(nova_string)
print(nova_string1)






