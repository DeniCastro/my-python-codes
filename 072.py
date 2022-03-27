# Números por extenso.

# Cria a variável que exibe os números por extenso.
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Cria loop infinito para permitir a continuação do programa ou não.
while True:

    # Validação para ver se o número está dentro do limite
    while True:

        # Recebe número do usuário. Se menor que zero e maior que 20: interromper.
        número = int(input('Digite um número entre 0 e 20: '))
        if 0 <= número <= 20:
            break
        print('tente novamente: ', end='')

    # Printa o número digitado:
    print(f'Você digitou o número {cont[número]}')

    # Pergunta se o usuário deseja continuar na linha do segundo loop.(Fatiação necessária)
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break
print("Fim da operação.")
