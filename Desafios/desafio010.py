# Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos
# Dólares ela pode comprar.

dinheiro_carteira = float(input('Digite o quanto essa pessoa tem na carteira: R$'))
taxa_cambio = float(input('Digite a taxa de câmbio atual (R$ para US$): '))
compra_dolar = dinheiro_carteira / taxa_cambio
print(f'Com R${dinheiro_carteira:.2f}, essa pessoa pode comprar US${compra_dolar:.2f} usando a taxa de câmbio de R${taxa_cambio:.2f}.')