# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print(f"Nome com tudo maiúsculo: {nome.upper()}")
print(f"Nome com tudo minúsculo: {nome.lower()}")

print(f"Total de letras (sem espaços): {len(nome) - nome.count(' ')}")
# Outra forma de saber quantas letras ao todo sem espaços:print(f"Total de letras (sem espaços): {len(nome.replace(" ", ""))}")


primeiro_nome = nome.split()
print(f"Quantidade de letras no primeiro nome: {primeiro_nome[0]}, {len(primeiro_nome[0])} letras.")
#print(f"Quantidade de letras no primeiro nome: {nome.find(' ')}")
# print(f"Quantidade de letras no primeiro nome: {len(primeiro_nome.split()[0])}")