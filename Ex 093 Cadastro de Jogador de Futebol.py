lista = {}
gol = []
total = 0
lista['nome'] = input('Nome do jogador: ')
p = int(input(f'quantas partidas {lista["nome"]} jogou: '))
for c in range(0, p):
    gol.append(int(input(f'quantos gols na partida {c+1}?: ')))
    total += gol[c]
lista['gols'] = gol[:]
lista['total'] = total
print('-='*15)
for k, v in lista.items():
    print(f'o valor campo {k} tem o valor {v}')
print('-='*15)
print(f' o jogador {lista["nome"]} jogou {len(lista["gols"])} partidas')
for c in range(0,(len(lista['gols']))):
    print (f'na partida {c+1} , fez {lista["gols"][c]} gols.')
print(f'total de {lista["total"]} gols')
