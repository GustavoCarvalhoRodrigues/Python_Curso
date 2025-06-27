# Desenvolva um programa que leia as duas
# notas de um aluno, calcule e mostre a sua média.

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
print(f'A média desse aluno em relação as duas notas lançadas foi: {media:.1f}')