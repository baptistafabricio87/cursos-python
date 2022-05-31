

class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Objeto construido ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("\nSaldo: {} - Titular: {} ".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __valida_saldo(self, valor_do_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_do_saque <= valor_disponivel

    def saca(self, valor):
        if self.__valida_saldo(valor):
            self.__saldo -= valor
            print("Saque efetuado no valor:", valor)
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, c_destino, valor):
        if self.__valida_saldo():
            self.saca(valor)
            c_destino.deposito(valor)
            print("transferencia efetuada!")
        else:
            print("O valor {} passou o limite".format(valor))

    def get_numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


    @staticmethod
    def codigo_banco():
        return "001"


    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
