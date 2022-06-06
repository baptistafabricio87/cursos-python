from abc import ABCMeta, abstractmethod 

class Programa(metaclass = ABCMeta): 

    @abstractmethod 
    def __str__(self): 
        pass


class Prgm(Programa): 

    def __str__(self):
        return 'Metodo abstrato sobrescrito'


pgm = Prgm()
print(pgm)