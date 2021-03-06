class Funcionario:

    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostra_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando Cursos - {mes}'if mes else 'Mostrando cursos do mês')

class Alura(Funcionario):
    def mostra_tarefas(self):
        print('FEz muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas no forum.')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

class Senior(Hipster):
    pass


jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostra_tarefas()
print(luan)
print(jose)