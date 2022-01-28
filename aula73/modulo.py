def soma(x: float, y: float) -> float:
    return x + y

if __name__ == '__main__':  # se o modulo tiver sendo executado diretamente, executa os prints.
# se for importado não será mais executado junto da importação.
    print(soma(10, 20))
    print(soma(20, 20))

'o processo anterior também pode ser usado com uma função main. exemplo:'

def soma(x: float, y: float) -> float:
    return x + y

def main() -> None:
    print(soma(20, 50))
    print(soma(10, 50))

if __name__ == '__main__':
    main()

'serve para importar coisas sem se preocupar com as outras que não eram pra ser importadas'
