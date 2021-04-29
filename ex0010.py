#Desafio 10. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem nacarteira?R$'))
dolar = real / 5.70
print('com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))





