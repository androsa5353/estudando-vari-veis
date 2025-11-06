nome = str(input('Digite seu nome: ')).strip()
di = nome.upper()
di1 = nome.lower()
di2 = len(nome)-nome.count(' ')
di3 = nome.find(' ')
print(f'Seu nome em maíusculo é: {di} \nSeu nome em minusculo é: {di1} \n{di2} \n{di3}')

