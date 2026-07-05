frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} veses' .format(frase.count('A')))
print('A posição da primeira letra A é {}' .format(frase.find('A') +1))
print('A ultima posição da letra A é {}' .format(frase.rfind('A') +1))
