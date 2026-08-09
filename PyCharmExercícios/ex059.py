from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
menu = 0

while menu != 5:
    print('''>>>>>>>>>>>>>MENU<<<<<<<<<<<<<    
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    menu = int(input('>>>>>>> Qual é a sua opção? '))

    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif menu == 2:
        multiplicador = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicador))

    elif menu == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        else:
            print('Os números {} e {} são iguais'.format(n1, n2))

    elif menu == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))

    elif menu == 5:
        print('Saindo do programa...')

    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('FIM DO PROGRAMA')
