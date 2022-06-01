class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.likes} Likes')


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes')

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.temporadas} temp - {self.likes} Likes')