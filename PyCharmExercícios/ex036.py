vc = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o seu salário? R$'))
anos = int(input('Quantos anos deseja pagar? '))

# Calcula o número total de meses (anos * 12)
prestacoes = anos * 12

# Calcula o valor de cada prestação mensal
valor_prestaçao = vc / prestacoes

# Condição: a prestação não pode exceder 30% do salário
limite_salario = s * 30 / 100

if valor_prestaçao > limite_salario:
    print('Emprestimo NEGADO! o valor da prestação execede 30% do seu salário.')
else:
    print('Emprestimo APROVADO! A prestação sera de R${:.2f}'.format(valor_prestaçao))
