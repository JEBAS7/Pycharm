l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
c = l * a
qt = c / 2
print('Sua parede tem a dimenção de {:.2f}x{:.2f} e sua área é de {}m² é necessário {:.2f} litros de tinta'.format(l, a, c, qt))