

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Contruindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo: {} - Titular: {} ".format(self.saldo, self.titular))

    def cria_conta(numero, titular, saldo, limite):
        conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
        return conta


    def deposito(self, valor):
        self.saldo += valor


    def saca(self, valor):
        self.saldo -= valor

