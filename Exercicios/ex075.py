valores = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 apareceu {valores.index(3)+1} vezes'if 3 in valores else'Não foi digitado valor 3')
print('Os valores pares digitados foram', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
