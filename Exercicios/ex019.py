import random
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
lista = [a,b,c,d]
primeiro = random.choice(lista)
print(f'o primeiro aluno vai ser {primeiro}')