# Ler o primeiro termo e a razão de uma PA. Mostrando os 10 primeiros termos.

print('GERADOR DE PA')
print('=-' * 10)
primeiro = int(input('Digite o primeiro termo: '))      # lê o primeiro termo.
razão = int(input('Digite a razão da PA: '))             # Lê a razão.
termo = primeiro                                        # Cria uma variável pro primeiro termo.
cont = 1                                                # Cria um contador de termos que começa pelo 'PRIMEIRO' termo.
while cont <= 10:                                       # O "10" vêm do que foi pedido no enunciado.
    print(f'{termo} → ', end='')
    termo += razão
    cont += 1
print('FIM!')
