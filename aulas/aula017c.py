teste = list()
teste.append('André')
teste.append(24)
gente = list()
gente.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
gente.append(teste[:])
print(gente)