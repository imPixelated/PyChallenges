# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample

sort = sample(['pablo','marcos','roberto', 'samuel'], k=4 )
print(sort)

