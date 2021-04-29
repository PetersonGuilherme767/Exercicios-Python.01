#Ex.0026 - Faça um programa que leia uma frase pelo teclado e mostre
#Quantas vezes aparece letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

