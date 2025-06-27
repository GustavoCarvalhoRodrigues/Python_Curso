# Escreva um programa que pergunte a quantidade
# de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60 por dia e
# R$0.15 por km rodado.

q_km_percorridos = float(input('Digite a quantidade de km percorridos por um carro alugado: '))
q_dias_alugado = float(input('Digite a quantidade de dias que o carro foi alugado: '))
preco_pagar = (60 * q_dias_alugado) + (q_km_percorridos * 0.15)
print(f'Com {q_km_percorridos} km percorridos e {q_dias_alugado} dias alugado, o preço a pagar é R${preco_pagar:.2f}  ')

