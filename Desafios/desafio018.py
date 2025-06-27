# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = int(input('Digite um ângulo qualquer: '))

seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'Ângulo: {angulo}°')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {coss:.2f}')
print(f'Tangente: {tang:.2f}')

