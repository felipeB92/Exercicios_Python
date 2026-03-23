import random
import time
lista = []

def sorteia(a):
    for c in range(0,5):
        d = random.randrange(0,9)
        a.append(d)
    print('sorteando numeros',end=' ')
    for c in range(0,5):
        time.sleep(0.5)
        print(a[c],end=' ')

def somapar(a):
    soma = 0
    for s in a:
        if s % 2 == 0:
            soma += s
    print(f'\na soma dos numeros pares é {soma}')

sorteia(lista)
somapar(lista)




