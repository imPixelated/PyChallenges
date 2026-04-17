# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas e minusculas
# Quantas letras ao todo (sem contar espaços)
# Quantas letras tem o primeiro nome

nome = input("Qual seu nome completo? ")
print("Analisando nome...")

print(f"Seu nome em maiusculo fica {nome.upper()}")
print(f"Seu nome em minusculo fica {nome.lower()}")

print(f"O seu nome inteiro possui: {len(nome.replace(" ", ""))} letras!")
print(f"Seu primeiro nome tem: {len(nome.split()[0])} Letras!")
