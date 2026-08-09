palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar',
    'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiouáàâãéêíóôõú':
            print(letra.lower(), end=' ')
