import math
n = int(input('digite um numero: '))
c = n
f =[]
o = 0
while n!=0:
    if c==n:
        o=c
        f.append(o)
        n+=-1
    else:
        o=c-n
        f.append(o)
        n+=-1

lista = list(f)
lista.sort(reverse=True)
listaX = 'X'.join(map(str,lista))
p = math.prod(lista)
print ('{}! = {} = {}'.format(lista[0],listaX,p))


