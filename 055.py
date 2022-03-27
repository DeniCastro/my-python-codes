# Leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0          # Estabelecer valores em 0 para duas variáveis faz com que nada mais alem do inserido seja analisado.
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:     # Analisa o peso da primeira pessoa, fazendo com que seja o maior e menor peso.
        maior = peso
        menor = peso
    else:
        if peso > maior:       # Transforma o novo valor inserido no maior peso se for maior.
            maior = peso
        if peso < menor:       # Transforma o novo valor inserido no menor peso se for menor.
            menor = peso
print(f'O maior peso lido foi {maior}.')
print(f'O menor peso lido foi {menor}.')
