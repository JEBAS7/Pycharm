#Minha solução
'''a = int(input('Digite um ano: '))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('O ano {} é bissexto!'.format(a))
else:
    print('Esse ano {} não é bissexto!'.format(a))'''

#Solução do professor
from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))