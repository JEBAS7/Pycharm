def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
print()
print('-' * 30)
nome = str(input('Nome do Jogador: ')).strip()
gols_input = str(input('Número de Gols: ')).strip()

# Validação do número de gols
if gols_input.isnumeric():
    gols = int(gols_input) # Só converte para int se forem apenas números
else:
    gols = 0 # Se o usuário deu Enter ou digitou letras, vira 0

# Validação do nome
if nome == '':
    ficha(gol=gols) # Passa apenas o gol, o nome assume o padrão '<desconhecido>'
else:
    ficha(nome, gols)
