#Faça um algaritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
preço = float(input('Qual é o preço: R$'))
novo = preço - preço * 5 / 100
print('O produto que custava R${}, com desconto de 5% vai custar R${:.2f}'.format(preço, novo))





