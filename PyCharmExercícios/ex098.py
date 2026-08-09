from time import sleep


def contador(inicio, fim, passo):
    # Tratamento do passo zero ou negativo
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)  # Transforma o passo negativo em positivo

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.5)

    # Caso 1: Contagem Crescente
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')

    # Caso 2: Contagem Decrescente
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


# --- PROGRAMA PRINCIPAL ---

# 1. Duas contagens obrigatórias do desafio
contador(1, 10, 1)
contador(10, 0, 2)

# 2. Parte personalizada (fora da função)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

# Envia os dados lidos do teclado para a função trabalhar
contador(ini, fim, pas)
