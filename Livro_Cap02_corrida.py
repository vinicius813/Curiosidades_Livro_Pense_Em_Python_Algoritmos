# Hora inicial da partida
print('Encontre o tempo para tomar café da manhã:')
hora_1 = float(input('Digite aqui a hora exata da partida: '))

# Subtrações de tempo
km_1 = hora_1 + 8.15
km_3 = km_1 + 7.12
km_2 = km_3 + 8.15
hora_break = km_1 + km_3 + km_2

# Hora do café da manhã
print('A hora exata para o café da manhã será: ', hora_break)