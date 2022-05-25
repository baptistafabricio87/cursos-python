

def jogar():
    palavra_secreta = 'banana'
    letras_certas = ['_', '_', '_', '_', '_', '_']
    letras_faltando = str(letras_certas.count('_'))
    enforcou = False
    acertou = False

    print(letras_certas)
    print(f'Ainda falta {letras_faltando} letras.')
    while not enforcou and not acertou:
        chute = input('Qual letra ?  ')
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_certas[index] = letra
            index += 1

        print(letras_certas)

        letras_faltando = str(letras_certas.count('_'))
        if letras_faltando == '0':
            acertou = True
            print('Parabens! Se salvou!!!')
        elif len(letras_faltando) < len(letras_certas):
            print(f'Ainda falta {letras_faltando} letras.')
        else:
            enforcou = True
            print('Enforcou! :p')

if __name__ == '__main__':
    jogar()
