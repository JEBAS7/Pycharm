print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)

lista = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90)

# O passo 2 pula de dois em dois para separar produto de preço
for pos in range(0, len(lista), 2):
    produto = lista[pos]
    preco = lista[pos + 1]
    print(f'{produto:.<40}R${preco:>7.2f}')
print('-' * 50)
