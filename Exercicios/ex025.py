nome = str(input('Digite seu nome completo: ')).strip()
two = 'silva' in nome.lower()
#two = nome[:].upper() == 'Silva'
print(f'Existe Silva nesse nome? {two}')
