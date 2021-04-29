#Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m

larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('Sua parede tem a dimenção de {}x{} e sua area é de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisara de {}L de tinta.'.format(tinta))


