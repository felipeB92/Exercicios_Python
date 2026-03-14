import random
n=random.randint(0,10)
t= 0
p =""
while p != n:
    p= int(input('digite um numero de 0 a 10: '))
    t += 1
    if t != n:
        print('\033[1;31merrou tente de novo\033[m')
        if p>10:
            print('\033[1;31mde 0 a 10\033[m')
print('parabens voce acertou na {}º tentativas'.format(t))
