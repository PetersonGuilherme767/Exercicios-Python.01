#Ex.0027 - Faça um programa que leia o nome completo de uma pessoa mostrandon o primeiro nome e o último separadamente

nome = str(input('Digite seu nome:')).strip()
print('Óla {}, prazer em te conhecer'.format(nome))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
