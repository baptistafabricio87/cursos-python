class Programa:

    def __init__(self, nome, ano, duracao):
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
    def duracao(self):
        return self.__duracao
    
    @property
    def likes(self):
        return self.__likes
    
    @likes.setter
    def likes(self, likes):
        self.__likes += likes


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super(nome, ano)
        self.__duracao = duracao


class Serie:

    def __init__(self, nome, ano, temporadas):
        super(nome, ano)
        self.__temporadas = temporadas