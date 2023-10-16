'''Desafio - Crie um programa que:
Escolhe um numero secreto.
Pede por um chute do usuário.
Indica se o usuário acertou ou não.
Se não acerto, dá uma dica, dizendo se o numero é mais alto ou mais baixo.
Repete isso até 3 vezes!'''

numero_secreto=5
chute1=0
chute2=0
chute=int(input("Tente adivinhar um numero de 0 a 10 \n Qual seu palpite? "))
if chute != numero_secreto:
    if chute < numero_secreto:
        chute1=int(input('Você errou, seu palpite é menor que o numero secreto! \nTente novamente: '))
        if chute1 < numero_secreto:
            chute2=int(input('Você errou, seu palpite é menor que o numero secreto! \nTente novamente: '))
            if chute2 != numero_secreto:
                print('Infelizmente você errou novamente.\nObrigado por jogar!')
            else:
                print('Parabéns, você acertou!')
        elif chute1 > numero_secreto:
            chute2=int(input('Você errou, seu palpite é maior que o numero secreto! \nTente novamente: '))
            if chute2 != numero_secreto:
                print(f'Infelizmente você errou novamente o número secreto era {numero_secreto}.\nObrigado por jogar!')
            else:
                print('Parabéns, você acertou!')
        else:
            print('Parabéns, você acertou!')
    elif chute > numero_secreto:
        chute1=int(input('Você errou, seu palpite é maior que o numero secreto! \nTente novamente: '))
        if chute1 < numero_secreto:
            chute2=int(input('Você errou, seu palpite é menor que o numero secreto! \nTente novamente: '))
            if chute2 != numero_secreto:
                print('Infelizmente você errou novamente.\nObrigado por jogar!')
            else:
                print('Parabéns, você acertou!')
        elif chute1 > numero_secreto:
            chute2=int(input('Você errou, seu palpite é maior que o numero secreto! \nTente novamente: '))
            if chute2 != numero_secreto:
                print(f'Infelizmente você errou novamente o número secreto era {numero_secreto}.\nObrigado por jogar!')
            else:
                print('Parabéns, você acertou!')
        else:
            print('Parabéns, você acertou!')
else:
    print('Parabéns, você acertou!')
print('Fim de jogo')