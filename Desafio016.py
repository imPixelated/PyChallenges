# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math
ang = float(input('Digite o valor do angulo: '))
tan = math.tan(math.radians(ang))
cos = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))

print(f"Aqui estão o Seno, Cosseno e Tangente do seu Angulo! \nSeno: {seno:.3} \nCosseno: {cos:.3} \nTangente: {tan:.3}")
