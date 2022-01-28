import re

class CalcIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido.')

        self._ip = valor

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return
        if not self._valida_ip(valor):
            raise ValueError('Mascara inválida')

        self._mascara = valor
        self._mascara_bin = self._ip_to_binario(valor)
        print(self._mascara_bin)

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return

        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser inteiro.')

        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 Bits')

        self._prefixo = valor

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_binario(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x)) [2:].zfill(8) for x in blocos]
        return ''.join(blocos_binarios))