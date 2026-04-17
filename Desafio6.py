# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada;

n = int(input("Digite um número inteiro: "))

dobro = n * 2
triplo = n * 3
raiz = n ** 0.5

print("O seu número é: {} \n O Dobro de seu número é: {} \nO Triplo de seu número é {} \nA raiz quadrada de seu número é: {} ".format(n, dobro, triplo, raiz))