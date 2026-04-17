# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Qual o seu nome?')

print("O seu nome com todas as letras maiusculas fica:", nome.upper())
print("O seu nome com todas as letras minúsculas fica:", nome.lower())
print(f"Seu nome possui {len(nome.replace(' ', ''))} caracteres!")


