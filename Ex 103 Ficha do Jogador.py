def ficha(n='desconhecido',g=0):
    print(f'o jogador {n}  marcou {g} gols')


nome = input('qual nome do jogador?: ')
gols = input('quantos gols ele marcou?: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=g)
else:
    ficha(nome,gols)


