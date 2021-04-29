#Ex.0029 - Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite'''

c = int(input('Qual a velocidade do carro?'))
if c > 80:
    print('Multado! você excedeu o limite permitido que é 80km/h')
    m = (c - 80) * 7
    print('Você deve pagar uma multa de R${}'.format(m))
else:
    print('Tenha um bom dia, dirija com segurança!')
