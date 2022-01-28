class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado')
            return

        print(f'{self._nome} foi ligado')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self.nome} já está desligado')
            return

        print(f'{self._nome} foi desligado')
        self._ligado = False