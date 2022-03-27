# Crie um caixa eletrônico que exiba quantas cédulas de cada tipo eu utilizei.

print('=' * 30)
print('{:^30}'.format('BANCO DO BOSTIL'))
print('=' * 30)

# Recebe valor de saque e dá esse valor para a variável total.

valor = int(input('Quanto deseja sacar? '))
total = valor

# Cria variável para cédulas e uma para o seu total(A mais alta seria de 50).

cédulas = 50
totalDeCédulas = 0

# Cria loop infinito, com esse código, conseguimos ver quantas cédulas de 50 podemos tirar do total.
while True:
    if total >= cédulas:     # Se o total atual for maior ou igual ao valor da cédula(50).
        total -= cédulas     # O total será o total menos o valor dessa cédula de 50.
        totalDeCédulas += 1  # Soma mais um pro número de cédulas usadas para esse valor.

    # Se não:
    else:
        # Faz com que só seja exibido se a cédula seja utilizada.
        if totalDeCédulas > 0:
            print(f'total de {totalDeCédulas} de R$ {cédulas}.')

        # Se a cédula for 50, eu não poderei remover esse valor, então atribuo o próximo valor à variável cédulas.
        if cédulas == 50:
            cédulas = 20
        elif cédulas == 20:  # Repete para cédulas de 20
            cédulas = 10
        elif cédulas == 10:  # Repete para cédulas de 10
            cédulas = 1
        totalDeCédulas = 0
        if total == 0:       # Se o total zerar, interrompe o loop.
            break
print('Fim da Operação')
