# Faça um programa que leia a largura e a altura de uma parede em metros
# Calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

a = int(input("Digite a Altura da parede:"))
l = int(input("Digite a Largura da parede:"))

area = a * l
tinta = area / 2


print("A area da parede é {}".format(area))
print("Você precisará de {} tinta para pintar".format(tinta))



