n50 = 0
n20 = 0
n10 = 0
n1  = 0
while True:
    n=int(input('qual valor pretende sacar: '))
    n50 = n//50
    if n % 50 != 0:
        n20 = (n%50)//20
    if n % 20 != 0:
        n10 = (n%20)//10
    if n % 10 != 0:
        n1 = n%10
    break
print('seu valor sacado em notas sera')
if n50 > 0:
    print(f'{n50} notas de 50 Reais')
if n20 > 0:
    print(f'{n20} notas de 20 Reais')
if n10 > 0:
    print(f'{n10} notas de 10 Reais')
if n1 > 0:
    print(f'{n1} notas de 1 Real')
print('obrigado por usar nosso banco volte sempre')

