numero1 = input('digite um numero: ')
numero2 = input('digite outro numero: ')

# isnumeric isdigit isdecimal - essas funções podem ajudar para n ter erro no programa, no caso do usuário digitar uma letra no lugar de um número
# números e positivos (123456)
print(numero1.isnumeric())  # checa se pode ser convertido para um numero inteiro, retorna false ou true

if numero1.isdigit() and numero2.isdigit():  # se os dois forem um digito posso converter a string para int e fazer a soma
    numero1 = int(numero1)
    numero2 = int(numero2)

    print(numero1 + numero2)

else:
    print('não pude converter os números')

# essa condição não é valida para números boleando, nesse caso existe uma solução. abordagem da próxima aula



