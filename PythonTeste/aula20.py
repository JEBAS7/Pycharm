def lin():
    print('-' * 30)

# Programa Principal
lin()
print('     CURSO EM VIDEO    ')
lin()
print('     APRENDA PYTHON     ')
lin()
print('     GUSTAVO GUANABARA      ')
lin()

def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

# Programa Principal
título('     CURSO EM VIDEO    ')
título('     APRENDA PYTHON     ')
título('     GUSTAVO GUANABARA      ')

def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f'soma A + B = {s}')


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores: {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
