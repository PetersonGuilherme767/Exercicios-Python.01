#Ex.0017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um Triângulo Retângulo calcule e mostre o comprimento da Hipotenusa

#Incluindo importação
from math import hypot
o = float(input('Digite o cateto oposto:'))
a = float(input('Digite o cateto adjacente:'))
h = hypot(a, o)
print('resultado:{:.1f}'.format(h))










