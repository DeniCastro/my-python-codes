# Jogue par ou ímpar com o computador. O jogo só será interrompido quando você perder. Mostrando o total de vitórias
# consecutivas que ele conquistou.

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o pc {computador}. Total de {total}', end='')
    print(' e DEU PAR' if total % 2 == 0 else ' e DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Vc Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'game over! Você venceu {v} vezes.')

"""
Importe randint
Crie variável vazia para contar as vitórias.
Inicia o While sem range.
Cria variável do Jogador e recebe valor que o jogador escolher.
Cria variável computador com range de escolha.
Cria variável de tipo sem strings, somente espaço
Cria while para receber a escolha do tipo Par ou Impar → recebe a escolha (Fatie a String e Deixe Maiúscula).
Exibe as escolhas e o total. Diga se deu PAR ou ÍMPAR
Caso o tipo seja P e for par → exiba que o jogador venceu e some às vitórias.
Caso contrário, exiba que o jogador perdeu e interrompa o laço
Repita com ímpar usando "E SE." *Observação:"SE" e "E SE" principais estão na linha de While.
Ainda na linha do segundo "Enquanto", Exiba que vai jogar novamente.
Na última linha, exiba o fim de jogo e total de vitórias.
"""
