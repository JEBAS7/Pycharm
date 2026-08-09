s = float(input('Digite o salário do funcionario R$'))
#novo = s + (s * 15 / 100)
a = s * 0.10
b = s * 0.15
salarioa = s + a
salariob = s + b
salario_max = 1250
if salarioa > salario_max:
    salario_max = salarioa
    print('Novo salário do funcionário R${:.2f}'.format(salarioa))
if salariob <= salario_max:
    print('Novo salário do funcionário R${:.2f}'.format(salariob))