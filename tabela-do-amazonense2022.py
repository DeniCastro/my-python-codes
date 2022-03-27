# Tabela do Campeaonato Amazonense.

times = ('Nacional', 'São Raimundo', 'Fast Clube', 'Manaus FC', 'Amazonas FC', 'Princesa do Solimões', 'Penarol',
         'Manauara FC', 'Clipper', 'Operário FC')

print('=-' * 61)
print(f'Lista de times: {times}')
print('=-' * 61)
print(f'Os cinco primeiros colocados são:  {times[0:5]}')
print('=-' * 61)
print(f'Os 4 últimos são: {times[-4:]}')
print('=-' * 61)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 61)
print(f'A posição do naça é: {times.index("Nacional")+1}ª posição.')
print('=-' * 61)
