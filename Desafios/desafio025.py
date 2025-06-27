# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite um nome: ")).strip()

print(f"Essa pessoa tem SILVA no nome: {'SILVA' in nome.upper()}")