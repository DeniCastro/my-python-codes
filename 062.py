# Melhore o exercício 61, perguntando se o usuário quer mostrar mais termos, termine quando o usuario escolher 0.

print('GERADOR DE PA')
print('=-' * 10)
primeiro = int(input('Digite o primeiro termo: '))    # lê o primeiro termo.
razão = int(input('Digite a razão da PA: '))          # Lê a razão.
termo = primeiro                                      # Cria uma variável pro primeiro termo.
cont = 1                                              # Cria um contador de termos que começa pelo 'PRIMEIRO' termo.
total = 0                                             # Possibilita o cálculo dos termos.
mais = 10                                             # É onde começa o programa.
while mais != 0:                                      # mais deve ser diferente de 0 para continuar perguntando.
    total += mais                                     # O total a ser mostrado somará com o que foi requerido.
    while cont <= total:                              # Enquanto a contagem for menor ou igual ao total...
        print(f'{termo} → ', end='')
        termo += razão                                # O termo irá fazendo a contagem com base na razão selecionada.
        cont += 1                                     # Adiciona mais um pra contagem.
    print('PAUSA')
    mais = int(input('Escolha mais termos: '))
print(f'Progressão finalizada com {total} termos mostrados.')
