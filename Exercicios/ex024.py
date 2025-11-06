cidade = str(input('Digite sua cidade: '))
one = cidade[:5].upper() == 'SANTO'
#one = 'santo' in cidade
print(f'Contém a palavra santo na cidade? {one}')