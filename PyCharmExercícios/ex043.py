peso = float(input('Digite o seu peso? (Kg) '))
altura = float(input('Digite sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('PARABENS! Seu IMC é {:.1f}, você está com peso normal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}, você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}, você está com obesidade.'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f}, voce está com obesidade mórbida.'.format(imc))
