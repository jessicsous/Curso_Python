from da_aula56 import Carrinhodecompras, Produto

carrinho = Carrinhodecompras
p1 = Produto('camisa', 50)
p2 = Produto('sandália', 20)
p3 = Produto('celular', 1000)
p4 = Produto('boneca', 70)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())