valores = []
while True:
    # 1. Leia como TEXTO primeiro (remova o int daqui)
    n = input('Digite um valor: ').strip()

    # 2. Agora o .isnumeric() funciona perfeitamente no texto
    if not n.isnumeric():
        print('Você digitou um valor inválido!')
        continue  # Volta para o início do laço

    # 3. Converta para número APÓS ter certeza de que é seguro
    n = int(n)

    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in p:
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')
