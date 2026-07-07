n1 = float(input('Digite uma nota de 0 a 10: '))
n2 = float(input('Digite uma nota de 0 a 10: '))
m = (n1 + n2)/2
if n1 > 10 or n2 > 10:
    print('ERRO! Você digitou uma nota {} ou {} maior que 10!'.format(n1, n2))
    exit()
if m >= 7:
    print('A média do aluno foi {}, o aluno está APROVADO!'.format(m))
elif m >= 5 and m < 7:
    print('A média do aluno foi {}, o aluno está em RECUPERAÇÃO!'.format(m))
else:
    print('A média do aluno foi {}, o aluno está reprovado!'.format(m))