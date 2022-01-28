class MinhaClasse:
    """Documentação normal
    
    Conforme qualquer outra documentação que você tenha usado anteriormente.
    """""
    atributo = 1
    atributo = 'Valor'

    def __init__(self, texto):
        """inicializa os dados
        
        :param texto: o texto da classe
        :type texto:str
        """""
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """ Método que exibe um texto de 100 caracteres na tela

        :param texto: Um texto de 100 caracteres
        :type texto: str

        :return: O texto de 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypepeError: Se o texto não for uma string


        :param texto:
        :return:
        """