# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente
# Ex: Ana Maria de Souza
# Primeiro: Ana
# último: Souza

nome = input('Diga seu nome completo:').strip()
nome = nome.split()
print(f"Seu primeiro nome é {nome[0]}!\nSeu último nome é {nome[-1]}!")