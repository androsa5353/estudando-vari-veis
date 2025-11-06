#import random
from random import shuffle
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('terceiro aluno: ')
d = input('Quarto aluno ')
escolhidos = [a, b, c, d]
shuffle(escolhidos)
print('a ordem de apresentação será: ')
print(escolhidos)