from banco import Banco
from desafio1 import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Jessica', 24)
cliente2 = Cliente('Lucas', 21)
cliente3 = Cliente('marcela', 25)

conta1 = ContaPoupanca(1111, 234567, 0)
conta2 = ContaCorrente(2222, 234566, 0)
conta3 = ContaPoupanca(3333, 234565, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print()

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')