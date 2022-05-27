from conta import Conta
from pessoa import Pessoa
conta1 = Conta(1, "Fabricio", 500.0)

print("Extrato ")
conta1.extrato()

print("\nSaque ")
conta1.saca(40.0)
print("Extrato ")
conta1.extrato()

print("\nDeposito")
conta1.deposito(50.0)
print("Extrato ")
conta1.extrato()

pessoa1 = Pessoa("Fabricio", "Castro")

print("Objeto Pessoa")
pessoa1.exibe_nome()