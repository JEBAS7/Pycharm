def leiaInt(msg):
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            numero = int(numero)
            if numero >= 0:  # Colocamos a validação do número correto aqui dentro
                return numero
        else:
            # Trocamos o 'return' por 'print' para o loop NÃO parar!
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n = leiaInt('Digite um numero inteiro: ')
print(f'Você acabou de digitar o número {n}')
