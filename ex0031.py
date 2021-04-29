#Ex.0031 - Desenvolva um prograna que pergunte a distância de uma viagem em km e calcule o preço da passagem
#cobrando R$0.50 por km para viagens até 200km e R$0,45 para viagens mais longas

distância = float(input('Qual a distancia da sua viagem?'))
p1 = distância * 0.50
p2 = distância * 0.45
if distância <= 200:
    print('Total a pagar R${:.2f}'.format(p1))
else:
    print('Total a pagar R${:.2f}'.format(p2))







