# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno_1 = input('Qual o nome do primeiro(a) aluno(a): ')
aluno_2 = input('Qual o nome do segundo(a) aluno(a): ')
aluno_3 = input('Qual o nome do terceiro(a) aluno(a): ')
aluno_4 = input('Qual o nome do quarto(a) aluno(a): ')
sortear = [aluno_1, aluno_2, aluno_3, aluno_4]
nome_escolhido = choice(sortear)
print(f'O aluno escolhido para apagar o quadro foi: {nome_escolhido}')


