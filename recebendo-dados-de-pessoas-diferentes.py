# Ler nome, idade e sexo de pessoas e mostrar média de idade, nome do homem mais velho e mulheres com menos de 20 anos.

# Antes do código principal, criamos variáveis que auxiliem na busca por valores do enunciado:
somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 4):
    print(f'======= {p}ª pessoa ======')            # Começa a contagem das pessoas.
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()
    somaidade += idade                              # Acrescenta valores nas idades apresentadas antes.
    if p == 1 and sexo in 'Mm':                     # "in" irá encontrar as letras sejam maiúsculas ou minúsculas.
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = somaidade / 3                               # A média é tirada fora do laço for.

print(f'A média de idade é de {media:.0f}.')        # ":.0f" irá formatar o float que fica nas idades.
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos que 20 anos.')

'''=================================================================================================================

Outra forma de reproduzir o código utilizando LISTAS:
lista_nome = []
lista_nome_homem = []
lista_idade = []
lista_sexo = []
lista_idade_homem = []
lista_idade_mulher = []

for c in range (1,5):
    print('-------------- {}ª pessoa ----------------'.format(c))
    nome = str(input('Digite o nome: ')).strip().upper()
    lista_nome.append(nome)

    idade = int(input('Digite a idade: '))
    lista_idade.append(idade)

    sexo = str(input('Digite o sexo M/F: ')).strip().upper()
    lista_sexo.append(sexo)

    if sexo == 'M':
        lista_nome_homem.append(nome)
        lista_idade_homem.append(idade)
    if sexo == 'F' and idade < 20:
        lista_idade_mulher.append(idade)

print('A média de idade do grupo é {}'.format(sum(lista_idade)/len(lista_idade)))
print('Nome do homem mais velho: {}'.format(lista_nome_homem[lista_idade_homem.index(max(lista_idade_homem))]))
print('O total de mulheres abaixo de 20 anos: {}'.format(len(lista_idade_mulher)))

================================================================================================================='''
