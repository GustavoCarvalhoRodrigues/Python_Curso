# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


v_carro = float(input('Qual foi a velociadade do carro: '))

if v_carro > 80:
    multa = 7 * (v_carro - 80)
    print(f"MULTADO!  está acima do limite de velocidade que é 80Km! \n Sua velocidade: {v_carro} Km/h \n Valor da multa: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade!")