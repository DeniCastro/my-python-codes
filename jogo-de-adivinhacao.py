# O computador irá pensar em um número de 0 a 10. Você deverá ficar tentando adivinhar ATÉ acertar!

from random import randint
computador = randint(0, 3)
print('Sou seu computador... Acabei de pensar em um número de 0 à 3.')
print('Será que consegue adivinhar qual foi?')
acertou = False                                  # Acertou recebe falso para começar a condição de vencer o jogo.
palpites = 0                                     # Cria a possibilidade de contar o número de palpites.
while not acertou:                               # Not cria a condição de não ter acertado.
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1                                # Imediatamente adiciona ao total de tentativas.
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:                 # Indica se está abaixo ou acima do que foi o palpite.
            print('MAIS... tente denovo!')
        elif jogador > computador:
            print('MENOS... tente denovo!')
print(f'Acertou com {palpites} tentativas.')
