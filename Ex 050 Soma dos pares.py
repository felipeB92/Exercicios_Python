s = 0
for c in range(0,6):
    n = int(input('digite um numero: '))
    if n % 2 == 0:
        p = n
        s += n
print (' a soma dos numeros pares é {}'.format(s))