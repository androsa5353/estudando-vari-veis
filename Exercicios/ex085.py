núm = [[], []]
valor = 0
for p in range(1, 8):
    valor = int(input(f'Digite o {p}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitador foram: {núm[0]}')
print(f'Os valores ímpares digitador foram: {núm[1]}')