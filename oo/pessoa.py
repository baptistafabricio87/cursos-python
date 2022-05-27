

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome(self):
        print("-> {} {} ".format(self.nome, self.sobrenome))
