# Faça um programa que leia um número inteiro e diga se ele é primo.

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')           # utiliza cores
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes', end='')    # end='' Continua na mesma linha
if tot == 2:
    print(' e por isso ele é primo!')
else:
    print(' e por isso ele não é primo!')
