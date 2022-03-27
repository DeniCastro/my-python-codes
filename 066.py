# Leia vários números inteiros e pare quando chegar no 999.

som = num = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1      # Conta somente após o input
    som += num     # Soma o total de números
print(f"Você digitou {cont} número e  total da soma foi {som}.")
