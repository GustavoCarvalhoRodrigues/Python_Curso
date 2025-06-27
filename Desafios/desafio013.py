# Faça um algoritmo que leia o salário
# de um funcionário e mostre seu novo salário,
# com 15% de aumento.

sal_func = float(input('Digite o salário desse funcionário: R$'))
novo_sal = sal_func + (sal_func * 0.15)
print(f'O salário atual desse funcionário é: R${sal_func:.2f}, com um aumento de 15%, o novo salário será: {novo_sal:.2f}')