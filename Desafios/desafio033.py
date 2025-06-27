
# Solicita os dados do usuário
valor_casa = float(input('Valor da casa: R$'))
sal_comprador = float(input('Salário do comprador: R$'))
anos_financiados = int(input('Quantos anos de financiamento? '))

# Cácula a prestação mensal
prestação = valor_casa / (anos_financiados * 12) 

# Calcula o valor máximo da prestação permitida (30% do salário)
limite = sal_comprador * (30 / 100) 

# Mostra os dados do financiamento
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_financiados:.0f} anos', end='')
print(f' a prestação será de R${prestação:.2f}')

# Verifica se o empréstimo pode ser concedido
if prestação <= limite: 
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
