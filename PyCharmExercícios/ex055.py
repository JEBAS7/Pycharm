maior = 0
menor = 0

# Altere o número 6 para ler mais ou menos pessoas
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))

#    minha solução para verificação do maior e menor IMC de um grupo de pessoas
#    altura = float(input('Digite a altura da {}ª pessoa? (m) '.format(c)))
#    imc = peso / (altura ** 2)

    # Na primeira repetição, o primeiro PESO é o maior e o menor
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso encontrado foi {:.1f}Kg'.format(maior))
print('O menor peso encontrado foi {:.1f}Kg'.format(menor))
