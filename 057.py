# Leia o sexo das pessoas em "M ou F". Caso esteja errado, peça a digitação novamente.

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor, informe corretamente seu sexo! ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
