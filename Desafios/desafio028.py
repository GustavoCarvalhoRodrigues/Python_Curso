# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)

pessoa = int(input('Em que número pensei? '))
print("PROCESSANDO...")
sleep(3)

print("-=-" * 20)
if pessoa == computador:
    print("O usuário venceu!")
else:
    print("O usuário perdeu!")
print("-=-" * 20)

