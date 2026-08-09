from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if ano >= atual:
    print('ERRO! Você digitou o ano {} atual ou acima.'.format(ano))
    exit()
if idade < 18:
    print('Você ainda não tem que se alistar! Você tem {} anos, em {} anos você pode alistar.'.format(idade, 18 - idade))
elif idade == 18:
    print('Você já pode se alistar!')
else:
    print('Você já passou da idade de alistamento, você tem {} anos, já passou {} anos para se alistar.'.format(idade, idade - 18))