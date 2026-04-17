# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num = (input("Digite um número de 0 até 9999: "))

print("O seu número é: {}".format(num))
print(f"O Número: {num[:1]} - é um Milhar!")
print(f"O Número: {num[1:2]} - é uma Centena!")
print(f"O Número: {num[2:3]} - é uma Dezena!")
print(f"O número: {num[3:4]} - é uma Unidade! ")



