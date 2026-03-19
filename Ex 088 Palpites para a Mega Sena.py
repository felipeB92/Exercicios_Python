import random
import time
lista = []
print('-='*5,'JOGOS MEGA SENA','-='*5)
n = int(input('quantos jogos deseja gerar: '))
for c in range(0, n):
    lista.clear()
    while True:
        if len(lista) == 6:
            break
        jogo = random.randint(1, 60)
        if jogo not in lista:
            lista.append(jogo)
    time.sleep(0.5)
    print(f'Jogo {c+1}: {lista}')
print('-='*6,'BOA SORTE','-='*6)
