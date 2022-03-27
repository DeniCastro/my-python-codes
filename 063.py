# Leia um número inteiro e mostre esses números na sequência de FIBONACCI.

n = int(input('Quantos termos deseja mostrar? '))     # Estipula o total de termos da sequência.
t1 = 0                                                # t1 e t2 São definidos automaticamente pois são o início dela.
t2 = 1
print(f'{t1} → {t2}', end='')                         # Cria a sequência na mesma linha.
cont = 3                                              # Cria contador de 3, os 2 primeiros termos já foram mostrados.
while cont <= n:                                      # Enquanto "cont" for menor que a variável do termo "n"...
    t3 = t1 + t2                                      # cria variável t3 cuja será o valor de t1 somado à t2.
    print(f' → {t3} ', end='')                        # Continua o t3 na mesma linha.
    t1 = t2                                           # Atribui novo valor pro t1, que será t2.
    t2 = t3                                           # Atribui novo valor pro t2, que será t3.
    cont += 1                                         # Começa a contagem enquanto estiver no limite de termos.
print('→ FIM!')
