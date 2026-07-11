números = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte'
)

while True:
    # Loop para garantir a digitação de um número válido
    while True:
        esc = int(input('Digite um número entre 0 e 20: '))
        if 0 <= esc <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'Você digitou o número {números[esc]}')

    # Loop para validação da resposta S/N
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('Programa encerrado. Até logo!')
