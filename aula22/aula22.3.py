# jogo da palavra secreta
# para revisao / aula 38

secreto = 'perfume'
digitadas = []
while True:
    letra = input('digite uma letra: ')
    if len(letra) > 1:
        print('por favor, digite apenas uma letra')
        continue
        digitadas.append(letra)

    if letra in secreto:
        print(f'uhuull, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'a letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    print(secreto_temporario)