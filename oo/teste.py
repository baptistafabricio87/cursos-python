from conta import Conta
from pessoa import Pessoa
from datas import Data


conta1 = Conta(1, "Fabricio", 500.0)
conta2 = Conta(2, "Tatiana", 400.0)

conta1.saca(1500.0)

# # EXEMPLO METODO ESTATICO
# print(Conta.codigo_banco())


# # EXERCICIO - PROPRIEDADES
# print("\nMostra limite: ", conta1.limite)
# x = float(input("Informe novo limite: "))
# conta1.limite = x
# print("Novo limite é: ", conta1.limite)

# # ENCAPSULAMENTO
# conta1.transfere(conta2, 50.0)
# conta2.extrato()

# # METODOS
# print("Extrato ")
# conta1.extrato()

# print("\nSaque ")
# conta1.saca(40.0)
# print("Extrato ")
# conta1.extrato()

# print("\nDeposito")
# conta1.deposito(50.0)
# print("Extrato ")
# conta1.extrato()

# # EXERCICIO 1
# pessoa1 = Pessoa("Fabricio", "Castro")
# print("\nObjeto Pessoa")
# pessoa1.exibe_nome()

# # EXERCICIO 2
# print("\nExercicio DATAS")
# d = Data(27, 5, 2022)
# d.dt_formatada()