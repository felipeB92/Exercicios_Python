import math
n = 0
q = 0
l=[]
while n != 999:
    n = int(input('digite um numero ou digite 999 para parar: '))
    if n != 999:
        l.append(n)
        q+=1
s = sum(l)
print ('os numeros que você digitou foram:')
print ('\033[1;31m{}\033[m'.format(l))
print ('um total de \033[1;31m{}\033[m digitos e a soma deles é \033[1;31m{}\033[m'.format(q,s))