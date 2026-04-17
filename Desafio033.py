# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

sal = float(input("Qual o seu salário? "))

if sal > 1250:
    aum = sal * 0.10
    print(f"O seu salário terá um aumento de: {aum:.2f}, totalizando {sal + aum:.2f} reais")
else:
    aum2 = sal * 0.15
    print(f"O seu salário terá um aumento de: {aum2:.2f}, totalizandob {sal + aum2:.2f} reais")