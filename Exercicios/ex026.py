frase = str(input('Digite uma frase: ')).upper().strip()
d1 = frase.count('A')
d2 = frase.find('A')+1
d3 = frase.rfind('A')+1
print(f' A letra A aparece: {d1} vezes \n A primeira letrar A apareceu na posição: {d2} \n A última letra A apareceu na posição: {d3}')
