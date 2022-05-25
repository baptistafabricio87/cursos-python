def jogar():
    palavra_secreta = 'banana'.upper()
    letras_certas = ['_' for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_certas)
    
    while not enforcou and not acertou:
        chute = input('Qual letra ?  ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_certas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_certas
        print(letras_certas)

    if acertou:
        print('Parabéns! Você acertou a palavra secreta', palavra_secreta)
    else:
        print('\nEnforcou! Fim de Jogo!')

if __name__ == '__main__':
    jogar()
