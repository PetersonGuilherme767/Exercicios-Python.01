#Faça um algaritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Qual é o seu salário: R$'))
a = s + (s * 15 / 100)
print('Com aumento de 15% seu salário é R${:.2f}'.format(a,))





