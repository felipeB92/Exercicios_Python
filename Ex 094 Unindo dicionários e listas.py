lista = []
dados ={}
q = ''
media = 0
while True:
    if q == 'N':
        break
    else:
        q = ''
        dados['nome'] = str(input('Nome: '))
        dados['idade'] = int(input('Idade: '))
        dados['sexo'] = str(input('Sexo: ')).upper()
        lista.append(dados.copy())
        dados.clear()
        while q !='S' and q !='N':
            q = str(input('Deseja continuar? [S/N] ')).upper()
print(15*'=-')
print(f'o grupo tem {len(lista)} pessoas cadastradas')
print('as mulheres cadastradas são',end=' ')
for c in lista:
    media += c['idade']
    if c['sexo'] == 'F':
        print(f'{c['nome']}',end=' ')
media = media/len(lista)
print()
print(f'a media de idade é {media} anos')
print('as pessoas que estão acima da media de idade são:')
print()
for c in lista:
    if c['idade'] > media:
        print(f'nome ={c["nome"]} Ideade={c["idade"]} sexo={c["sexo"]}')
        print(' ')
print(15*'=-')
