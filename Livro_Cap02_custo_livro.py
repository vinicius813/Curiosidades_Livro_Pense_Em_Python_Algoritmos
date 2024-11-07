# O cálculo inicial de um livro mais frete
preco_livro = print('Calcular o custo de um livro:')
livro = float(input('Digite aqui o valor da capa do livro: '))

# Entrega com descontos percentuais
desconto = 0.60 * livro
custo_1 = (0.75 * 59) + desconto
custo_final = custo_1 + livro

# Valor ou custo final do livro
print('O custo benefício do livro para atacado será: ', custo_final)
