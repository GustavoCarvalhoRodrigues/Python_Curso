# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

c_oposto = float(input('Digite o comprimento do cateto oposto: '))
c_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(c_oposto, c_adjacente)
print(f'Cateto oposto: {c_oposto} e Cateto adjacente: {c_adjacente} e sua Hipotenusa: {hipotenusa:.2f}')

