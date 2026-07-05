n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))

#Verificando o maior número
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

#Verificando o menor número
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
