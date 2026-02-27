def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} = {a}')


print(' Controle de terrenos')
print('-' * 20)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
área(l, c)