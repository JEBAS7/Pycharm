n1 = int(input('Digite um numero inteiro qualquer: '))
n2 = int(input('Digite um numero inteiro qualquer: '))
if n1 > n2:
    print('O primeiro número é maior {} que o segundo {}.'.format(n1, n2))
elif n1 < n2:
    print('O segundo número é maior {} que o primeiro {}.'.format(n2, n1))
else:
    print('Não exite valor maior, os dois são iguais.')
