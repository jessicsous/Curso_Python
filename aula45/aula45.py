# tratar excessões

try:
    a = {}
except NameError as erro:
    print('erro do desenvolvedor', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave')
except Exception as erro:
    print('ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente.')
print('continuar')
