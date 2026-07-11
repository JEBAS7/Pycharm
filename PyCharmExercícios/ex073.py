times = ('Palmeiras', 'Flamengo', 'Fluminense',
         'Athletico-PR', 'Red Bull Bragantino',
         'Bahia', 'Coritiba', 'São Paulo', 'Atlético-MG',
         'Corinthians', 'Cruzeiro', 'Botafogo', 'Vitória',
         'Internacional', 'Santos', 'Grêmio', 'Vasco',
         'Remo', 'Mirassol', 'Chapecoense')
print('-=' * 60)
print(f'Os cinco primeiros colocados {times[:5]}')
print('-=' * 60)
print(f'Os ultimos 4 colocados {times[-4:]}')
print('-=' * 60)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 60)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}ª posição ')
