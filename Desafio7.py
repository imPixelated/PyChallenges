# Desenvolva um programa que leia as duas notas de um aluno e calcule sua média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("A primeira nota do aluno é: {} \nA segunda nota do aluno é: {} \nA média do seu aluno é: {}".format(nota1, nota2, media))