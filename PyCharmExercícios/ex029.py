v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado em R${:.2f}!'.format((v - 80) * 7))
