import adivinhacao as adv
import forca as fc

def iniciar():
    print("*******************************")
    print("******** CONSOLE JOGOS ********")
    print("** (1) Forca (2) Adivinhação **")
    opc = int(input("Escolha sua opção: "))

    if opc == 1:
        fc.jogar()
    elif opc == 2:
        adv.jogar()
    else:
        print("Opção Inválida! Finalizando Console...")


if __name__ == '__main__':
    iniciar()
