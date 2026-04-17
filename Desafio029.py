# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

numero = int(input("Digite um numero: "))

resultado = numero % 2

if numero % 2 == 0:
    print(f"O número digitado: {numero} - é PAR! :D")
else:
    print(f"O número digitado: {numero} - é IMPAR :P")