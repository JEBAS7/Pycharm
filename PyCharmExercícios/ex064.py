n = int(input('Digite um numero [999 para parar]: '))
cont = 0
soma = 0
total_termos = 0
while n != 999:
    cont += 1
    total_termos += n
    soma += n
    n = int(input('Digite um numero [999 para parar]: '))
print('Foram digitados {} e a soma deles é {}'.format(cont, soma))
print('FIM DO PROGRAMA')
