#Ex.0035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro segmento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo!')
else:
    print('Os seguimentos acima não podem formar um triângulo!')
