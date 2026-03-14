p = ""
l = []
f = 0
while p != 'N':
    n = int(input('digite um numero: '))
    l.append(n)
    q = input('quer continuar [S/N]: ')
    f += 1
    p = q.upper()
l.sort()
soma = sum(l)
media = soma / f
print (l)
print ('o maior numero é {} e o menor {}'.format(l[-1],l[0]))
print ('media é {}'.format(media))