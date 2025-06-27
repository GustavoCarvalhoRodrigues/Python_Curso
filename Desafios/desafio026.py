# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite alguma frase: ")).upper().strip()

print(f"A quantidade de vezes que aparece letra A: {frase.count('A')}")
print(f"Qual a posição aparece a primeira vez a letra A: {frase.find('A')+1}")
print(f"Qual a posição aparece a última vez a letra A: {frase.rfind('A')+1}")