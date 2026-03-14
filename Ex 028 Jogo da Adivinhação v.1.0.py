import random
n1 = int(input('advinhe um numero entre 0 e 5: '))
n2 = random.randint(0,5)
if n1 == n2:
    print ('parabens o numero realmente é {} voce venceu'.format(n1))
else:
    print('pensei em {} infelizmente voce perdeu'.format(n2))
print ('até a proxima')
