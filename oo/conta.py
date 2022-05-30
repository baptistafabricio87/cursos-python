

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Objeto construido ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("\nSaldo: {} - Titular: {} ".format(self.__saldo, self.__titular))


    def deposito(self, valor):
        self.__saldo += valor


    def saca(self, valor):
        self.__saldo -= valor


    def transfere(self, c_destino, valor ):
        self.saca(valor)
        c_destino.deposito(valor)
    

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
