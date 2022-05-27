

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome(self):
        print("-> {0} {1} ".format(self.nome, self.sobrenome))

    