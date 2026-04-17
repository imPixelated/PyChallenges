# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

km = float(input("Quantos quilometros você estava? "))

if km > 80:
    print("Você foi multado!")
    km = (km - 80) * 7
    print(f"Sua multa foi de R${km:.2f}")
else:
    print("Tá de boa! Você não foi multado.")