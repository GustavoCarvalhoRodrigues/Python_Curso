# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

from random import shuffle

aluno_1 = input('Qual o nome do primeiro(a) aluno(a): ')
aluno_2 = input('Qual o nome do segundo(a) aluno(a): ')
aluno_3 = input('Qual o nome do terceiro(a) aluno(a): ')
aluno_4 = input('Qual o nome do quarto(a) aluno(a): ')
ordem_sorteada = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(ordem_sorteada)
print(f'A ordem de apresentação foi: {ordem_sorteada}')

