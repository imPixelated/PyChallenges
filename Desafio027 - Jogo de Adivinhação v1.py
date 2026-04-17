# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
from time import sleep

num = int(input("Escolha um número de 0 a 5: "))
num2 = [0, 1, 2, 3, 4, 5]
escolher = choice(num2)
print("Processando. . .")
sleep(3)

print(f"O Número em que pensei foi {escolher} e o Número que você escolheu foi {num}")
if num == escolher:
    print("Você ganhou!")
else:
    print("Você perdeu!")
