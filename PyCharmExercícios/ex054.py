from datetime import date

atual = date.today().year
maioridade = 0
menoridade = 0

for c in range(1, 8):
    ano = int(input('Qual o {}º ano de nascimento? '.format(c)))
    idade = atual - ano

    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

print('\nTotal de pessoas:')
print('Há {} pessoa(s) maior(es) de idade.'.format(maioridade))
print('Há {} pessoa(s) menor(es) de idade.'.format(menoridade))
