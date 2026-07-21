galera = list()
pessoa = dict()
soma = média = 0

# 1. ETAPA DE CADASTRO
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()

    # Validação do Sexo (Só aceita M ou F)
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    # Validação da idade só aceita numeros inteiros
    while True:
        try:
            pessoa['idade'] = int(input('Idade: '))
            break
        except ValueError:
            print('Por favor, digite um número inteiro válido! ')

    soma += pessoa['idade']  # Já vai somando as idades para a média

    galera.append(pessoa.copy())

    # Validação da Resposta (Só aceita S ou N)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)

# A) Total de pessoas
print(f'A) Ao todo, temos {len(galera)} pessoas cadastradas.')

# B) Média de idade
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')

# C) Lista de Mulheres
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}] ', end='')
print()  # Pula linha

# D) Pessoas com idade acima da média
print('D) Lista das pessoas que estão acima da média:\n')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        # Mostra os dados em linha formatada (estilo dicionário)
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print('\n')

print('<< ENCERRADO >>')
