def leiaInt(mensagem):
    while True:
        try:
            entrada = input(mensagem).strip()
            if entrada == '':  # Se o usuário apenas apertou Enter
                print('\033[31mERRO! O campo não pode ficar vazio.\033[m')
                continue
            n = int(entrada)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não terminar de digitar.\033[m')
            return 0
        else:
            return n


def leiaFloat(mensagem):
    while True:
        try:
            entrada = input(mensagem).strip().replace(',', '.')
            if entrada == '':  # Se o usuário apenas apertou Enter
                print('\033[31mERRO! O campo não pode ficar vazio.\033[m')
                continue
            n = float(entrada)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não terminar de digitar.\033[m')
            return 0
        else:
            return n


# Programa Principal
num_int = leiaInt('Digite um número Inteiro: ')
num_real = leiaFloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {num_int} e o real foi {num_real}')
