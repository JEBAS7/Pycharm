from datetime import date

trabalhador = {}

# 1. Coleta os dados básicos (não precisa de 'while True' para apenas 1 cadastro)
trabalhador['nome'] = str(input('Nome: ')).strip()
trabalhador['nascimento'] = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - trabalhador['nascimento']
trabalhador['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

# 2. Se tiver carteira de trabalho, coleta os dados adicionais
if trabalhador['carteira'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))

    # O cálculo correto da idade de aposentadoria:
    # Idade atual + (Ano em que vai se aposentar - Ano atual)
    ano_aposentadoria = trabalhador['contratacao'] + 35
    trabalhador['aposentadoria'] = trabalhador['idade'] + (ano_aposentadoria - date.today().year)

print('-=' * 20)

# 3. Exibe os resultados na tela de forma organizada
print(f' - Nome: {trabalhador["nome"]}')
print(f' - Idade: {trabalhador["idade"]} anos')
print(f' - CTPS: {trabalhador["carteira"]}')

# Só mostra os dados contratuais se a carteira for diferente de zero
if trabalhador['carteira'] != 0:
    print(f' - Ano de contratação: {trabalhador["contratacao"]}')
    print(f' - Salário: R$ {trabalhador["salario"]:.2f}')
    print(f' - Aposentadoria com: {trabalhador["aposentadoria"]} anos')

print('-=' * 20)
