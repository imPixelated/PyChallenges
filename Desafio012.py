# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = int(input("digite o preço do produto:"))
desconto = n - (n * 5 / 100)

print("O novo preço com desconto é {}".format(desconto))
