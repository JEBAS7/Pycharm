nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print('Seu nome completo é ', nome)
print('Seu nome em letras maúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('O primeiro nome é {} e tem {} letras'.format(nome, len(nome) - nome.count(' ')))

