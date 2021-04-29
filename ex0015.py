#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a qauntidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km.

dias = int(input('Quantos dias?'))
Km = float(input('Quantos Km percorridos?'))
r1 = (0.15 * Km) + (dias * 60)
print('O Total a pagar é de R${:.2f}'.format(r1))


