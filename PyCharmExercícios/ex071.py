print('=' * 30)
print(f'{'BANCO DO CEV':^30}')
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))

# Variáveis para contar o total de cada cédula
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

while True:
    # Tenta usar a cédula de 50
    if valor >= 50:
        valor -= 50
        ced50 += 1
    # Se não pode, tenta a de 20
    elif valor >= 20:
        valor -= 20
        ced20 += 1
    # Se não pode, tenta a de 10
    elif valor >= 10:
        valor -= 10
        ced10 += 1
    # Por fim, tenta a de 1
    elif valor >= 1:
        valor -= 1
        ced1 += 1

    # Se o dinheiro acabou, para o laço
    if valor == 0:
        break

print('=' * 30)
# Mostra apenas as cédulas que foram usadas
if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10')
if ced1 > 0:
    print(f'Total de {ced1} cédulas de R$1')

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
