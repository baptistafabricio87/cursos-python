
from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    
    
    def __getitem__(self):
        pass

    def __delitem__(self):
        pass

    def __len__(self):
        pass

    def __setitem__(self):
        pass

    def insert(self, index: int, value: _T) -> None:
        return super().insert(index, value)



objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)