r = 'S'
soma = quant = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    # Guarda o primeiro número digitado
    if quant == 1:
        maior = menor = n
    else:
        # Atualiza o maior ou o menor valor
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

# Faz a divisão apenas depois do programa terminar (fora do loop)
media = soma / quant
print('Você digitou {} números e a média dos valores foi {:.2f}'.format(quant, media))
print('O maior número foi {} e o menor número foi {}'.format(maior, menor))
print('FIM DO PROGRAMA')
