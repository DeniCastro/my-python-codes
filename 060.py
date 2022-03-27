# Ler número e calcular o Fatorial

n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1                                          # 1 é o fator nulo para multiplicação.
print(f'Calculando {n}! = ', end='')           # Exibe o número escolhido e continua com o próximo print.
while c > 0:                                   # Faz com que a conta pare em 1
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')   # Printa 'x' se C é maior que um e '=' se não for maior, ou seja, igual.
    f *= c                                     # Similar à "f = f * c",
    c -= 1                                     # Tira 1 do C
print(f'{f}')                                  # printa o fatorial ao fim dos prints anteriores

"""
IMPORTANTO DA BIBLIOTECA MATH:
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')


UTILIZANDO O FOR:
n = int(input('Digite um número para calcular o seu fatorial: '))
acumulador = 1
for n in range(n, 0, -1):     # O número "0" indica que irá parar no número 1 e "-1" Indica que será decrescente.
    acumulador *= n           # Similar à acumulador = acumulador * n
    for n in range(1, 0, -1):
        acumulador *= n
print('O fatorial dos números é {}'.format(acumulador))

"""
