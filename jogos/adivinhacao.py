import random as rdm


def verificar_num(chute, num_secret):

    acerto = chute == num_secret
    maior = chute > num_secret
    menor = chute < num_secret

    if acerto:
        print(f'Voce acertou, o numero é: {chute}')
        return True
    else:
        if maior:
            print('Você errou, o numero é menor \n')
            return False
        elif menor:
            print('Você errou, o numero é maior \n')
            return False


def jogar():
    print('************************************')
    print('* Bem vindo ao jogo de Advinhação! *')
    print('************************************\n')
    print('*****  Niveis de Dificuldade   *****')
    print('(1) Facil (2) Médio (3) Dificil')
    nivel = int(input('Escolha o nivel: '))

    total_tentativa = 0
    if nivel == 1:
        total_tentativa = 20
    elif nivel == 2:
        total_tentativa = 10
    else:
        total_tentativa = 5

    num_secret = rdm.randrange(1, 101)
    for rodada in range(1, total_tentativa + 1):
        print(f'Tentativa {rodada} de {total_tentativa}')
        chute = int(input("Digite digitar um numero entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print('Você deve digitar um numero entre 1 e 100!')
            continue

        certo = verificar_num(chute, num_secret)

        if certo:
            break
        else:
            rodada += 1

    print('Fim de jogo!')


if __name__ == '__main__':
    jogar()
