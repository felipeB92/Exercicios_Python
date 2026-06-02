from random import randint
from time import sleep

palavras = ["casa", "tempo", "trabalho", "cafe", "rua", "vida", "pessoas", "hoje", "cidade", "amigo",'teste']
e = randint(0,len(palavras)-1)
resultado = []
temp = []
chutes = []
vida = 6
espacos = len(palavras[e])
print (f'{espacos*"_ "}')
while True:
    cont = 0
    temp.clear()
    letra = input('escolha uma letra\n')
    chutes.append(letra)
    for c in palavras[e]:
        if c == letra:
            cont += 1
        for l in c:
            if l in chutes:
                temp.append(l)
            else:
                temp.append('_')
    if cont == 0:
        vida -=1
        print (f'voce errou voce tem mais {vida} chances')
    resultado.clear()
    resultado = temp[:]
    print(resultado)
    if '_' not in resultado:
        print('parabens voce acertou')
        break
    if vida == 0:
        break
print(f'GAME OVER \na palavra era {palavras[e]}')