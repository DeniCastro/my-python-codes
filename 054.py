# Crie um programa que leia o ano de nascimento de sete pessoas e mostre quantas são e não são maiores de idade.

from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for p in range(1, 8):
    nascimento = int(input(f'Em que ano a {p}ª pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ao todos, tivemos {total_maior} pessoas maiores de idade e ', end='')
print(f'{total_menor} pessoas menores de idade')
