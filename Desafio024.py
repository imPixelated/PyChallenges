# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

s1 = str(input("Digite qualquer coisa! ")).lower().strip()
# Alternativa:
# s1 = s1.replace(" ", "")

vezes = s1.count("a")
pos1 = s1.find("a")
pos2 = s1.rfind("a")
print(f"A letra 'A' aparece exatamente {vezes} Vezes! \nAparece pela primeira vez na posição: {pos1 + 1} \nAparece na última vez: {pos2 + 1}")
