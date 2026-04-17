# Desenvolva um programa que leia o comprimento de três rotas e diga ao usuário se elas podem ou não formar um triângulo
t1 = float(input("Qual o primeiro segmento do triangulo? "))
t2 = float(input("Qual o segundo segmento do triangulo? "))
t3 = float(input("Qual o terceiro segmento do triangulo? "))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print("Os segmentos podem formar um triangulo sim!")
else:
    print("Não dá pra formar um triangulo não :/")