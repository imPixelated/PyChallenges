# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor;

n = int(input("Digite um número inteiro:"))
suc = n + 1
ant = n - 1

print(" O seu número é: {} \n O Sucessor deste número será: {} \n O Antecessor deste número é: {}".format(n, suc, ant))

# Outro jeito de fazer isso é especificando a conta dentro do .format
# print("Analisando o valor {}, seu sucessor seria {} e seu antecessor seria {)".format(n, (suc+1), (ant-1)))
