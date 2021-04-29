#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

import math
an = float(input('Digite o ângulo que você deseja:'))
se = math.sin(math.radians(an))
print('O ângulo de {} tem Seno de {:.2f}'.format(an, se))
co = math.cos(math.radians(an))
print('O ângulo de {} tem Cosseno de {:.2f}'.format(an, co))
ta = math.tan(math.radians(an))
print('O ângulo de {} tem Tangente de {:.2f}'.format(an, ta))

