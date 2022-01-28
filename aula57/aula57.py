from da_aula57 import Cliente, Endereco

cliente1 = Cliente('Jéssica', 24)
cliente1.inserir_endereco('Manaus', 'AM')
print(cliente1.nome)
cliente1.lista_enderecos()
print()
del cliente1

cliente2 = Cliente('Lucas', 21)
cliente2.inserir_endereco('Santarém', 'PA')
print(cliente2.nome)
cliente2.lista_enderecos()
print()
del cliente2
