lista = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Misassol', 'Fluminense', 'Bahia', 'Botafogo', 'São paulo',
         'Bragantino', 'Corinthians', 'Grêmio', 'Vasco', 'AtéticoMG', 'Santos', 'Ceará', 'Fortaleza', 'Vitoria',
         'Internacional', 'Juventude','Sport')
print(f'Lista de times: {lista}')
print(f'Os 5 primeiros são {lista[0:5]}')
print(f'Os 4 ultimos são {lista[-4:]}')
print(f'Times em ordem alfabetica: {sorted(lista)}')
print(f'O Bahia está na {lista.index("Bahia")+1} Posição')