carrinho = []
carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 50))
'''
somar os valores dos produtos usando list comprehension
'''
total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)