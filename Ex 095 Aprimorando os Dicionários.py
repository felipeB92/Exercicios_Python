lista = []
dados = {}
gol = []
total = 0
id = 0
q = ''
while True:
    q = ''
    id += 1
    dados['id'] = id
    dados['nome'] = input('Nome do jogador: ')
    p = int(input(f'quantas partidas {dados["nome"]} jogou: '))
    dados['partidas'] = p
    for c in range(0, p):
        gol.append(int(input(f'quantos gols na partida {c+1}?: ')))
        total += gol[c]
    dados['gols'] = gol[:]
    dados['total'] = total
    lista.append(dados.copy())
    dados.clear()
    gol.clear()
    total = 0
    while q != 'N' and q !='S':
        q = input('Quer cadastrar outro jogador? [S/N] ').upper()
    if q == 'N':
        break
print('-='*30)
print(f'nº{2*' '}Nome{11*' '}Gols{26*' '}Total')
print('-'*60)
t = 0
q = 1
for c in lista:
    print(f'{c['id']}   {c["nome"]}{(15-(len(c['nome'])))*' '}{c["gols"]}{(10-c['partidas'])*'   '}{c["total"]}')
print('-'*60)
while t != 999:
    t = int(input('deseja ver qual jogador? digite o nº ou 999 para finalizar: '))
    if t <= len(lista) and t > 0:
        print (f'o jogador {lista[t-1]['nome']}')
        for c in lista[t-1]['gols']:
            print(f'na partida {q} fez {c} gols')
            q += 1
    elif t == 999:
        print('finalizando...')
    else:
        print('\033[1;31mJogador não cadastrado\033[m')
    print('-' * 60)

