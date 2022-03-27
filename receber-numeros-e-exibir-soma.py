# leia vários números inteiros parar somente quando for digitado 999, mostrar o total de números e sua soma.

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))        # Recebe o primeiro valor.
while núm != 999:                                              # Indica o que terminará a função.
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))    # Se o número digitado foi 999, considera "0" no total.
print(f'Você digitou {cont} números e a soma deles foi {soma}.')

'''
n = total = cont = 0     # Ambas variáveis possuem a mesma atribuição.
while n != 999:
    n = int(input('Digite um número inteiro ou 999 para parar: '))
    if n != 999:         # Se o total for diferente de 999...
        total += n       # "total = total + n"  // Adiciona o número inserido ao total
        cont += 1        # "cont = cont + 1" → Enquanto o laço estiver continuando. // Adiciona +1 número pra contagem.
print('Foram digitados {} números e a soma entre eles foi {}'.format(cont, total))
'''
