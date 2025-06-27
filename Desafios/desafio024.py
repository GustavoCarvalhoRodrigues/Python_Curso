# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”. 

n_cidade = str(input("Digite uma cidade: (começa ou não com SANTO)")).strip()

print(f" Começa com SANTO: {n_cidade[:5].upper() == 'SANTO'} ")

# print(f" Começa com SANTO: {n_cidade.upper().startswith("SANTO")} ")
