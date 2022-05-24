

def jogar():
    palavra_secreta = 'banana'
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input('Qual letra ?  ')
        chute = chute.strip()
        index = 1
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print('Letra {} na posicao {}'.format(letra, index))
            index += 1

    print('Fim do jogo')


if __name__ == '__main__':
    jogar()
