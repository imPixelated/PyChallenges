# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US 1,00 = 3,27 Reais

n = int(input("Digite quanto de dinheiro você tem!"))
dolar = n / 5.14

print("Você pode comprar {:.3} Dólares!".format(dolar))
