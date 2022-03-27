# Crie um programa que leia uma frase e diga se é um palíndromo.

frase = str(input('Digite uma frase: ')).strip().upper()     # STRIP/UPPER Cria espaço e transforma em maiúsculas
palavras = frase.split()    # divide a frase em palavras
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Palíndromo')
else:
    print('Não é palíndromo!')

'''  ------------------------------------------------------------------------------------------------------
Sem utilizar o for:

frase = str(input("Qual a sua frase? ").upper().replace(" ",""))
if frase == frase[::-1]:
    print('A frase é um palíndromo!')
else:
    print('Não é um palíndromo!')
---------------------------------------------------------------------------------------------------------'''
