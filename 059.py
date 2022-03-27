# Leia dois valores e mostre um menu. Seu programa deverá realizar  a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:                           # Permite que 5 finalize o programa.  Varia de acordo com o número de opções.
    print("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA""")
    opc = int(input('Qual sua opção? '))  # Cria a possibilidade de usar diferentes opções.
    if opc == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opc == 2:
        multiplicação = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicação}')
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número é {maior}')
    elif opc == 4:
        print('Informe os números novamente!')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif opc == 5:
        print('FINALIZANDO...')
    else:
        print('Opção Inválida! Tente novamente')
    print('=-=' * 13)
    sleep(1.2)
print('Fim do programa! Volte sempre...')
