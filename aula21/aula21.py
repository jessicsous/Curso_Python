'''
for in em python
interando strings com for
função range(start=0, stop, step=1)
laço for: utilizado para coisas finitas
'''

texto = 'python'
c = 0

# iteração com laço while infinito
while c < len(texto):
    print(texto[c])
    c += 1

# iteração com laço for finito
for letra in texto:  # para 'letra' em 'texto'
    print(letra)     # mostre a letra na tela

# iteração com for usando a função enumerate
for n, letra in enumerate(texto):
    print(n, letra)




