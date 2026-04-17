# Um prof quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
nomes = ["pablo","marcos","roberto"]
sortear = random.choice(nomes)

print(sortear)