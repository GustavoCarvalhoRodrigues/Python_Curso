# Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo a raiz quadrada.

num = int(input('Digite um número inteiro: '))
print('O número é {} \nO dobro é {} \nO triplo é {} \nA raiz quadrada é {:.0f}'.format(num, (num * 2), (num * 3), pow(num, 1/2)))