# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# Cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('Quantos km percorridos: '))

if km < 200:
    km = km * 0.50
    print(f"O valor da sua viagem será: R${km:.2f}")
else:
    km = km * 0.45
    print(f"O valor da sua viagem será: R$2{km:.2f}")