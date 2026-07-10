# Inicialização correta dos contadores numéricos
pessoa = 0
tot18 = 0
tot_homens = 0
tot_mulheres20 = 0

while True:
    print('-' * 30)
    print('    CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))

    # Validação simples para aceitar apenas M ou F
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    # Lógica de contagem baseada nos requisitos finais
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F' and idade < 20:
        tot_mulheres20 += 1
    # conta pessoas
    pessoa += 1

    print('-' * 30)

    # Validação simples para aceitar apenas S ou N
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('======== FIM DO PROGRAMA =========')
print('=-' * 20)
print(f'Total de pessoas cadastradas: {pessoa}')
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tot_homens} homens cadastrados.')
print(f'E temos {tot_mulheres20} mulheres com menos de 20 anos.')
print('=-' * 20)
