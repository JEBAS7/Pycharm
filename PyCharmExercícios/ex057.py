#solução do professor
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

# minha solução
'''sexo = ' '
while sexo not in 'MmFf':
    sexo = str(input('informeseu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        print('Sexo masculino registrado com sucesso!')
    elif sexo == 'F':
        print('Sexo feminino registrado com sucesso!')
    else:
        var = sexo != '[Mm/Ff]'
        print('Escolha invalida! por favor digite apenas M ou F')'''
