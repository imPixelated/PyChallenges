# Crie um Programa que leia o nome de uma cidade e diga se começa ou não com o nome "Santo"

cidade = (input('Digite o nome de uma cidade: '))

cidade = cidade.lower()
cidade.replace(' ', '')
print(cidade[:5] == "santo")

# Alternativa:
# if 'Santo' in cidade:
#     print("A Cidade tem santo no nome!")
# else:
#     print("Não tem grr!")