s = c = 0
while True:
    n = int(input('digite um numero (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s}!')
