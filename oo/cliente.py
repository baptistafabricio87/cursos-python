

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("metodo get nome")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("metodo set nome")
        self.__nome = nome
