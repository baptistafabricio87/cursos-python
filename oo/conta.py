

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Contruindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo: {} - Titular: {} ".format(self.__saldo, self.__titular))


    def deposito(self, valor):
        self.__saldo += valor


    def saca(self, valor):
        self.__saldo -= valor


    def transfere(self, c_destino, valor ):
        self.saca(valor)
        c_destino.deposito(valor)
    

    def get_numero(self):
        return self.__numero


    def get_titular(self):
        return self.__titular


    def get_saldo(self):
        return self.__saldo
    

    def get_limite(self):
        return self.__limite

    
    def set_limite(self, limite):
        self.__limite = limite
