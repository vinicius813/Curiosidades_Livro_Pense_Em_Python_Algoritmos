# Começo da questão
print('Digite a transformação em milhas nos seguintes dados:')
bitcoin = float(input('Escreva o número de milhas: '))

# Valores no SI
milhas_segundo = bitcoin / 2562
milhas_minutos = bitcoin / 42.18
milhas_horas = bitcoin / 0.88
milhas_total = milhas_segundo + milhas_minutos + milhas_horas

# Imprimir resultado
print('A quantidade final de milhas é: ', milhas_total)