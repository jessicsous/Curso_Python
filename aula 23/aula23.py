'''
for / else em python
'''
variavel2 = ['jessica', 'joia', 'joelho']
comeca_j: False
for valor2 in variavel2:
    if valor2.lower().startswith('j'):  # converte maiuculo p/ minusculo
        comeca_j = True
if comeca_j:
    print('existe uma palavra que começa com j.')
else:
    print('não existe uma palavra que começa com j.')

# outra maneira
variavel3 = ['ajoelho', 'ajoia', 'ajessica']
for valor2 in variavel3:
    if valor2.lower().startswith('j'):
        break
else:
    print('não existe uma palavra q começa com j')

# outra maneira
variavel4 = ['jessica', 'silva', 'joia', 'joelho']
for valor4 in variavel4:
    if valor4.lower().startswith('j'):
        continue
    print(valor4)





