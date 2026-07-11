lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutaveis
# lanche[1] = 'refrigerante'
print(lanche)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[1:3])
print(lanche[-2])
print(lanche[:2])
print(lanche[2:])
print(lanche[-3:])
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print(sorted(lanche))
print(lanche)
a = (1, 2, 3, 4, 5)
b = (5, 6, 7, 8, 9)
c = a + b
print(a)
print(b)
print(c)
pessoa = ('Gustavo', 39, 'M', 99,88)
print(pessoa)
