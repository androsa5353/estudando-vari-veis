km = float(input('Qual a quantidade de km: '))
dias = int(input('Quantos dias foi alugado: '))
aluguel = (dias * 60) + (km * 0.15)
print(f'Eu vou pagar R${aluguel:.2f}')