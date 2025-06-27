# Faça um algoritmo que leia o preço
# de um produto e mostre seu novo preço, com
# 5% de desconto.

preco_produto = float(input('Digite o preço desse produto: '))
preco_novo_produto = preco_produto - (preco_produto * 0.05)
print(f'O preço desse produto é: R${preco_produto:.2f}, já com 5% de desconto será: R${preco_novo_produto:.2f}')