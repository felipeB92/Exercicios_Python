import random
import time
import operator
jogo = {'jogador 1': random.randint(1, 6),
    'jogador 2': random.randint(1, 6),
     'jogador 3': random.randint(1, 6),
     'jogador 4': random.randint(1, 6),}
print('-'*40)
for k,v in jogo.items():
    time.sleep(0.5)
    print (f'O jogador {k} tirou {v}')
rank = {}
rank = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('-'*40)
print(5*'-','Ranking dos jogadores',5*'-')
for c in range(0,4):
    time.sleep(0.5)
    print(f'O {c+1}º lugar foi {rank[c][0]} com {rank[c][1]} pontos.')
print('-'*40)