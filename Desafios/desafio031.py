# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d_viagem = float(input('Qual a distância de uma viagem percorrida em km: '))

p_viagem = d_viagem * 0.50 if d_viagem <= 200 else d_viagem * 0.45
print(f"Essa viagem percorreu: {d_viagem}Km, então o valor foi R${p_viagem:.2F}")
    