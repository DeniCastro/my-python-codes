# Mostre a tabuada de vários números, um de cada vez e interrompa se ele for negativo.

while True:
    n = int(input("Quer ver a tabuada de qual valor? "))  # Adiciona um valor para n
    if n < 0:
        break
    for c in range(1, 11):                                # Cria a condição de produto
        print(f"{n} x {c} = {n*c}")                       # Multiplica n pelo número do range
print('THE END!')
