notas = []  # Lista principal que guardará todos os alunos

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2  # Calcula a média deste aluno específico

    # Guarda os dados organizados: [Nome, [Nota1, Nota2], Média]
    notas.append([nome, [n1, n2], m])

    p = ' '
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).strip().upper()
        if p == '':  # Proteção para o ENTER vazio
            p = ' '
        else:
            p = p[0]

    if p == 'N':
        break

print('-=' * 30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

# Mostra a tabela de médias de todos os alunos
for i, aluno in enumerate(notas):
    # aluno[0] é o Nome, aluno[2] é a Média
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 30)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break

    # Verifica se o número digitado corresponde a um aluno válido na lista
    if n <= len(notas) - 1:
        # notas[n][0] busca o nome do aluno na posição digitada
        # notas[n][1] busca a lista de notas [nota1, nota2] daquele aluno
        print(f'Notas de {notas[n][0]} são {notas[n][1]}')
    else:
        print('Aluno não encontrado! Tente novamente.')

print('<<< VOLTE SEMPRE >>>')
