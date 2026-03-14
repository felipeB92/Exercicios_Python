s = 0
for c in range (1,500,2):
    if c % 3 == 0:
        n = int(c)
        s += n
print('a soma dos valores foi {}'.format(s))