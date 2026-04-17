# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = int(input("Digite um valor em metros para a conversão: "))
cent = n * 100
mil = n * 1000

print("Conversão\n Centímetros: {}cm\n Milimetros: {}cm".format(cent, mil))