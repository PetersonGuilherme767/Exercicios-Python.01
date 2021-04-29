#Ex.0028 - Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para
#o usuário tentar descobrir qual foi o número escolhido pelo computador
#o programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep
c = randint(0, 5)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
j = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(2)
print('Eu pensei no número {}'.format(c))
if j == c:
    print('Parabéns você acertou!')
else:
    print('Você errou, tente novamente')






