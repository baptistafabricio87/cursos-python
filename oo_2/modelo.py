class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas
