# Ler idade e sexo de várias pessoas, continuar ou não e mostrar maiores de 18, homens e mulheres com menos de 20 anos.

tot18 = totH = totM20 = 0                    # Exibe variáveis
while True:                                  # Inicia o While em loop.
    idade = int(input('Idade: '))            # Recebe idade e sexo(string Vazia pois ainda receberá input).
    sexo = ' '
    while sexo not in 'MF':                  # Cria segundo While e agora sim recebe o tipo(fatiado e maiúsculo).
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:                          # Se for maior de 18 → mais um pro tot18, se for M → recebe +1 pro totH
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:           # Se for Mulher e com menos de 20 → +1 pro totM
        totM20 += 1
    resp = ' '                               # Estipula variável para resposta se vai continuar e cria WHILE pra SIM/NÃO
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]   # Lembra de Fatiar e deixar maiúscula.
    if resp == 'N':                          # Se for negativa, interrompe e printa os resultados.
        break
print(f'O total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
