#Ex.0034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00 calcule um aumento de 10%
#Para salário inferiores ou iguais o aumento é de 15%

salário = float(input('Digite o salário:'))
s = salário * 10 / 100 + salário
i = salário * 15 / 100 + salário
if salário >= 1250:
    print('Com aumento de 10% seu salário passa a ser R${:.2f}'.format(s))
else:
    print('Com aumento de 15% seu salário passa a ser R${:.2f}'.format(i))

