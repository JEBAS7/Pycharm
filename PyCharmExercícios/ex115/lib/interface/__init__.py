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


def linha(tam = 40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[;33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32m Sua opção: \033[m')
    return opc

