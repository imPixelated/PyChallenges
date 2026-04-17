# Escreva um programa que leia dois números inteiros e compare-os
# Mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print(f"O Valor {n1} é maior que o {n2}!")
elif n1 == n2:
    print(f"Os dois valores {n1} e {n2} são exatamente iguais!")
else:
    print(f"O valor {n2} é maior que o {n1}!")