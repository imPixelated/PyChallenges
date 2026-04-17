# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = int(input("Qual o seu salario?"))
aum = sal + (sal * 15 / 100)

print(f"O seu salário atual é {sal} \n Com aumento de 15% fica {aum}")