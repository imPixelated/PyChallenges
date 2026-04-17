# Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import floor
num = float(input("Digite um valor real: "))
inteiro = floor(num)

print(f"O número inteiro do seu número real {num} é {inteiro}")
