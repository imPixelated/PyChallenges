# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Qual o seu nome? ')
print(f"Tem silva no nome? {"silva" in nome.lower()}")

# Alternativa
# if nome.find('silva') != 1:
#    print("Você tem Silva no nome!")
# else:
#    print("Você não tem Silva no nome!")