valores = []

for c in range(0, 5):
    n = input('Digite um valor: ')
    if not n.isnumeric():
        print('Você digitou um valor inválido!')
        continue
    n = int(n)

    # Se for o primeiro número (lista vazia) OU se for maior que o maior número atual
    if len(valores) == 0 or n > valores[-1]:
        valores.append(n)  # Adiciona no final
        print('Adicionado ao final da lista...')
    else:
        # Se ele não for o maior, vamos procurar a posição certa (do começo para o fim)
        posicao = 0
        while posicao < len(valores):
            if n <= valores[posicao]:
                valores.insert(posicao, n)  # Insere exatamente na posição do número maior
                print(f'Adicionado na posição {posicao} da lista...')
                break  # Para o while, pois já achou o lugar
            posicao += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {valores}')
