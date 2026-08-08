def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            numero = int(numero)
            if numero >= 0:  # Colocamos a validação do número correto aqui dentro
                return numero
        else:
            # Trocamos o 'return' por 'print' para o loop NÃO parar!
            print('\033[91mERRO! Digite um número inteiro válido.\033[m')
