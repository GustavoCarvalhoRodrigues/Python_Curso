# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n_completo = str(input("Digite um nome completo: ")).strip()
nome = n_completo.split()
print(f"Primeiro nome: {nome[0]}")
print(f"Último nome: {nome[len(nome) - 1]}")

#print(f"Último nome: {nome[-1]}")