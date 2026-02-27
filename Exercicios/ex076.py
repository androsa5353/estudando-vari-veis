lista = ('Lápis', 1.60,
         'Borracha', 3,
         'Lapiseira', 5,
         'Caderno', 25,
         'Livro', 30,
         'Estojo', 9.50,
         'Corretivo', 7.30,
         'Canetas', 21.80,
         'Mochila', 210.43,)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<15}', end='')
    else:
        print(f'R${lista[item]:.2f}')