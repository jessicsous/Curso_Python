print()
print('texto explicativo')


perguntas = {
    'pergunta 1': {
        'pergunta': 'quanto é 1+1? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '2',
        },
        'resposta_certa': 'c',
    },
    'pergunta 2': {
        'pergunta': 'quanto é 2*2? ',
        'respostas': {
            'a': '5',
            'b': '4',
            'c': '9',
        },
        'resposta_certa': 'b',
    },
}
print()

respostas_certas = 0
for chave_p, chave_r in perguntas.items():
    print(f'{chave_p}: {chave_r["pergunta"]}')

    print('respostas: ')
    for rk, rv in chave_r['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == chave_r['resposta_certa']:
        print('resposta certa!')
        respostas_certas += 1
    else:
        print('resposta errada!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'você acertou {respostas_certas} perguntasj.')
print(f'sua porcentagem de acerto foi de {porcentagem_acerto}%')