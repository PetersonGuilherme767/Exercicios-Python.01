#Escreva um programa que leia um valor em metros e o exiba em centimetro e milimetros.

m = int(input('Quantos metros você deseja converter?'))
c = m * 100
mi = m * 1000
print('{} metros equivale a {} Centimetros'.format(m, c))
print('{} metros equivale a {} milimetros'.format(m, mi))

