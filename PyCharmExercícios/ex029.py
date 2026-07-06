#minha solução.
'''v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado em R${:.2f}!'.format((v - 80) * 7))'''

#Solução do professor.
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você exedeu o limite permitido que de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
