# Gere 5 números aleatórios e coloque-os em uma tupla, mostre a listagem de números gerados e indique maior e menor.

from random import randint

# Para criar uma variável composta, adicione parêntesis:
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')

# laço for para gerar os números:
for n in números:
    print(f'{n} ', end='')

# Usa os métodos MAX e MIN para receber o maior e o menor valor.
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
