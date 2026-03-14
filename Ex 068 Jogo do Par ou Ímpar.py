import random
cont = 0
while True:
    n = int(input('escolha um numero: '))
    t = input('escolha par ou impar[P/I]: ').upper()
    r = random.randint(1, 10)
    if (n+r) % 2 == 0:
        rt = 'P'
        v = ('par')
    else:
        rt = 'I'
        v = ('impar')
    if t == rt:
        print(f'Eu esolhi {r} e voce {n}, {r+n} é {v}')
        print('voce \033[1;32mvenceu\033[m')
        cont += 1
        q = input('Quer continuar?[S/N]').upper()
        if q == 'N':
            print(f'voce venceu um total de {cont} vezes')
            break
    else:
        print(f'Eu esolhi {r} e voce {n}, {r+n} é {v}')
        print('voce \033[1;31mperdeu\033[m')
        print(f'voce venceu um total de {cont} vezes')
        break
print('GAME OVER')

