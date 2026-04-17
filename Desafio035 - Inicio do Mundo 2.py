# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar:
# O valor da casa, o salário do comprador e em quanto anos ele vai pagar.
# Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

# Aqui estão as perguntas que irão definir as variáveis ⤵︎
valor = float(input('Qual é o valor da casa? '))
sal = float(input("Qual é o seu salário? "))
anos = int(input("Em quantos anos você irá pagar? "))

# Aqui estão as variáveis, já com as contas pré-feitas ⤵︎
meses = anos * 12
mensal = valor / anos
limite = sal * 0.30

print('-=' * 30)
print(f"Você terá uma mensalidade de {meses} meses! Que são exatamente {anos} Anos!")
print(f"Sua mensalidade será de R${mensal:.2f} por mês")
print(f"30% do seu salário é: R${limite:.2f} - Isso quer dizer que:")
sleep(1) # Timerzinho para ficar bonitinho :D
print(f"Analisando...\n") # Isso não tá analisando nada, é apenas visual.
sleep(3) # Timerzinho pra ficar bonitinho :D

# Condicionais :P

if mensal < limite: # Se o valor da mensalidade for menor que o valor do limite, então...
    print("Você consegue comprar esta casa! ✅")
elif mensal == limite: # Se o valor da mensalidade for exatamente igual ao do limite, então...
    print("Wow! Foi raspando, mas você pode comprar esta casa! ✅")
else: # Ou se você não se enquadrar em nenhum dos critérios acima, isso acontece:
    print("Você não consegue comprar esta casa! ❌")

