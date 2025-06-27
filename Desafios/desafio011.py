# Faça um programa que leia a largura e a altura
# de uma parede, em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m^2.

largura_parede = float(input('Digite a largura dessa parede: '))
altura_parede = float(input('Digite a altura dessa parede: '))
area = largura_parede * altura_parede
q_tinta = area / 2
print(f'A área dessa parede é: {area:.3f} m²')
print(f'A quantidade de tinta necessária para pintar essa parede é: {q_tinta:.4f} litros')