lista =[]
dicionario = {}
dicionario['nome'] = str(input('Digite o nome do aluno: '))
dicionario['media'] = float(input(f'Digite media do {dicionario["nome"]}: '))
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
else:
    dicionario['situacao'] = 'Reprovado'
lista.append(dicionario)
for v , i in dicionario.items():
    print(f'{v} é igual a {i}')