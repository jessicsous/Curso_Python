print()
print('escreva a letra que corresponde a resposta certa')

pergunta = {
    'questão 1' : {
        'pergunta' : 'qual das expressões abaixo vai imprimir hello wold! na tela? ',
        'resposta' : {
            '(a)' : 'print(hello wold!)',
            '(b)' : 'def("hello wold!")',
            '(c)' : "print('hello wold!')",
            '(d)' : 'print "hello wold!"',
        },
        'resposta_certa' : 'c',
    },
    'questão 2' : {
        'pergunta' : 'qual classe pertence o numero 1.5? ',
        'resposta' : {
            '(a)' : 'str',
            '(b)' : 'int',
            '(c)' : 'bool',
            '(d)' : 'float',
        },
        'resposta_certa' : 'd',
    },
    'questão 3' : {
        'pergunta' : 'quais operadores abaixo representa uma exponenciação? ',
        'resposta' : {
            '(a)' : '**',
            '(b)' : '//',
            '(c)' : '/',
            '(d)' : '%',
        },
        'resposta_certa' : 'a',
    },
    'questâo 4' : {
        'pergunta' : 'qual símbolo abaixo representa uma lista? ',
        'resposta' : {
            '(a)' : '[]',
            '(b)' : '{}',
            '(c)' : '()',
            '(d)' : '""',
        },
        'resposta_certa' : 'a',
    },
    'questão 5' : {
        'pergunta' : 'qual função abaixo é responsável por definir função? ',
        'resposta' : {
            '(a)' : 'print',
            '(b)' : 'def',
            '(c)' : 'tupla',
            '(d)' : 'bool',
        },
        'resposta_certa' : 'b',
    },
}
print()
resposta_certa = 0
for chave_p, chave_r in pergunta.items():
    print(f'{chave_p} : {chave_r["pergunta"]}')

    print(f'respostas: ')
    for k, v in chave_r['resposta'].items():
        print(f' {k} : {v}')

    resposta_usuario = input('digite a resposta correta: ')

    if resposta_usuario == chave_r['resposta_certa']:
        print('resposta certa!')
        resposta_certa += 1
    else:
        print('resposta errada')

    print()
qtd_perguntas = len(pergunta)
porcentagem_acerto = resposta_certa / qtd_perguntas * 100

print(f'você acertou {resposta_certa} perguntas')
print(f'sua porcentagem de acertos foi {porcentagem_acerto}%')








