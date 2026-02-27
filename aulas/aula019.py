pessoas = {'nome': 'André', 'sexo': 'M', 'idade': 24}
pessoas['peso'] = 72
#del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())