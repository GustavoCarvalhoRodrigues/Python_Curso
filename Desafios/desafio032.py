# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Ano atual
    
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) # Cálculo do ano BISSEXTO
print( "É BISSEXTO!" if bissexto  else "Não é BISSEXTO!" )