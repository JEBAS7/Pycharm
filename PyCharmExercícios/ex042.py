r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

# Condição de existência do triângulo
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    # Classificação do triângulo
    if r1 == r2 == r3:
        print('Este triângulo é equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Este triângulo é isósceles')
    else:
        print('Este triângulo é escaleno')
else:
    print('Estas retas não formam um triângulo')
