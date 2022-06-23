# Projeto para estudo do paradigma Orientado a Objetos com Python3

## Temas Abordados

> ### Conceitos de Classe e Objeto
>
> - Construtor
> - Atributo / Propriedade
> - Metodo

---

### Construção de Metodos

- ***Metodo Construtor:***

> A definição dos atributos é feita no corpo do construtor, todos devem ser precedidos da palavras `self.` que faz referencia ao objeto, semelhante a palavra `this` em Java. Além de também utilizar a palavra reservada `__init__` para definir o metodo construtor.
>
>```python
>   def __init__(self, atr_a, atr_b, atr_c="xxx"):
>       self.__atr_a = atr_a
>       self.__atr_b = atr_b
>       self.__atr_c = atr_c
>```
>
>---

- ***Metodos Privados:***

> Utilizado como metodo interno, é representado com '__' (2 underscore) antes da nome do metodo, somente para utilização da classe, como por exemplo, um metodo que faz alguma validação, ou regra de negócio que não precisa e/ou não deve ficar exposto para utilizar fora da classe.
>
>```python
>   def __valida_saldo(self, valor_do_saque):
>       valor_disponivel = self.__saldo + self.__limite
>       return valor_do_saque <= valor_disponivel
>```
>
>---

- ***Metodos Estaticos:***

> Bastante útil quando necessário para leitura de informação da classe sem necessidade de instanciação da mesma. Porém deve ser utilizado com muito cuidado para se perder e sair do paradigma Orientado a Objetos.
>
>```python
>   @staticmethod
>   def metodo_estatico():
>       return {'normalmente' : 'dado', 'fixo' : 'quando', 'for' : 'necessário'}
>```
>
>---
