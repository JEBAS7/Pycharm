from datetime import date
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if ano >= atual:
    print('ERRO! Você digitou o ano {} atual ou acima.'.format(ano))
    exit()
if idade <= 9:
    print('Atleta MIRIM! Com a idade de {} anos.'.format(idade))
elif idade <= 14:
    print('Atleta INFANTIL! Com a idade de {} anos.'.format(idade))
elif idade <= 19:
    print('Atleta JUNIOR! Com a idade de {} anos.'.format(idade))
elif idade <= 25:
    print('Atleta SENIOR! Com a idade de {} anos.'.format(idade))
elif idade > 25:
    print('Atleta MASTER! Com a idade de {} anos.'.format(idade))
