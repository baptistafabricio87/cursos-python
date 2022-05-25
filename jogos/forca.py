import random as rdm


def marca_chute_certo(palavra_secreta, chute, letras_certas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_certas[index] = letra
        index += 1


def pede_chute():
    chute = input('\nQual letra ?  ')
    chute = chute.strip().upper()
    return chute


def mensagem_inicial():
    print('*************************************')
    print('***  Bem vindo ao Jogo da Forca!  ***')
    print('*************************************\n')


def escolhe_palavra():
    print("**************************************")
    print("Defina o tipo de palavra para o jogo!")
    print("(1) Frutas | (2) Nomes ")
    print("**************************************")
    print("Caso não escolha o tipo de palavra,\n\
        o tipo será o padrão Palavras.")
    print("**************************************\n")
    resp = int(input("Qual tipo de palavra você quer ?"))

    if resp == 1:
        arquivo = 'frutas.txt'
    elif resp == 2:
        arquivo = 'nomes.txt'
    else:
        arquivo = 'palavras.txt'

    return arquivo


def carrega_palavra(nome_arquivo="palavras.txt", primeira_linha_valida=0):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = rdm.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicia_letras_certas(palavra):
    return ['_' for letra in palavra]


def mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("*****************************")
    print("*     _________________     *")
    print("*    /                 \    *")
    print("* /\/                   \/\ *")
    print("* \ |   XXXX     XXXX   | / *")
    print("*  \|   XXXX     XXXX   |/  *")
    print("*   |   XXX       XXX   |   *")
    print("*   |                   |   *")
    print("*   \__      XXX      __/   *")
    print("*     |\     XXX     /|     *")
    print("*     | |           | |     *")
    print("*     | I I I I I I I |     *")
    print("*     |  I I I I I I  |     *")
    print("*      \__         __/      *")
    print("*         \_______/         *")
    print("*                           *")
    print("*****************************")


def mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("**************************")
    print("*       ___________      *")
    print("*      *._==_==_=_.*     *")
    print("*      .-\\:      /-.     *")
    print("*     | (|:.     |) |    *")
    print("*      '-|:.     |-'     *")
    print("*        \\::.    /       *")
    print("*         '::. .'        *")
    print("*           ) (          *")
    print("*         _.' '._        *")
    print("*        '-------'       *")
    print("**************************")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    enforcou = False
    acertou = False
    erros = 0

    mensagem_inicial()
    arquivo = escolhe_palavra()
    palavra_secreta = carrega_palavra(arquivo)

    letras_certas = inicia_letras_certas(palavra_secreta)
    print(letras_certas)

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_certo(palavra_secreta, chute, letras_certas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_certas
        print(letras_certas)

    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)


if __name__ == '__main__':
    jogar()
