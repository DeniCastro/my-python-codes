""" Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no
intervalo de 1 até 500."""
# para começar a contar os números começando de pares, se usa 0 na primeira pos. após o range
# para começar a contagem dos números começando de ímpares, usa 1 na primeira pos.

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores que são ímpares é {soma}')
