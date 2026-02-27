from uteis import moedaex107



p = float(input('Digite o preço:R$'))
print(f'A metade de {p} é {moedaex107.metade(p)}')
print(f'O dobro de {p} é {moedaex107.dobro(p)}')
print(f'Aumentando 10%, temos {moedaex107.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moedaex107.reduzir(p, 13)}')