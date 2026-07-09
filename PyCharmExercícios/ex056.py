somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Soma todas as idades para calcular a média depois
    somaidade += idade

    # Identifica o homem mais velho
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    # Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

# Calcula a média de idade do grupo
mediaidade = somaidade / 4

print('\nA média de idade do grupo é de {} anos.'.format(mediaidade))
if nomevelho != '':
    print('O homem mais velho é o {} e tem {} anos.'.format(nomevelho, maioridadehomem))
else:
    print('Não foi cadastrado nenhum homem no grupo.')
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totmulher20))
