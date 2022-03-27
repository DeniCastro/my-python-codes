# leia vários números, tire a média e exiba o maior e menor valor, perguntar se deseja continuar a digitar.
resp = 'S'
média = soma = quant = maior = menor = 0
while resp in 'Ss':            # Enquanto a resposta estiver em S maiúsculo ou minúsculo...
    núm = int(input('Digite um número: '))                          # Lê os números digitados
    soma += núm                # Faz com que minha soma receba mais um número.
    quant += 1                 # Adiciona um número à minha quantidade.
    if quant == 1:             # Se a quantidade de valores for igual a 1...
        maior = menor = núm    # O maior é a mesma coisa que o menor, que é o próprio número.
    else:                      # Se não...
        if núm > maior:        # Se o número for maior que o maior...
            maior = núm        # O maior número passará a ser "núm".
        if núm < menor:        # Se o número for menor que o menor...
            menor = núm        # O menor passará a ser "núm".
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]  # remove as letras e deixa em maiúsculo.
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média:.1f}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
