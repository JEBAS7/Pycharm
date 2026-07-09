maior = 0
menor = 0

# Altere o número 6 para ler mais ou menos pessoas
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa? (Kg) '.format(c)))
    altura = float(input('Digite a altura da {}ª pessoa? (m) '.format(c)))
    imc = peso / (altura ** 2)

    # Na primeira repetição, o primeiro IMC é o maior e o menor
    if c == 1:
        maior = imc
        menor = imc
    else:
        if imc > maior:
            maior = imc
        if imc < menor:
            menor = imc

print('O maior IMC encontrado foi {:.2f}'.format(maior))
print('O menor IMC encontrado foi {:.2f}'.format(menor))
