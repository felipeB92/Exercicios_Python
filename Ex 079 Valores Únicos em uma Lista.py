lista = []
q =0
while True:
    n = int(input('Digite um numero: '))
    if n in lista :
        print('\033[1;31m este numero ja foi digitado\033[m')
    else:
        lista.append(n)
    while True:
        q = input('deseja continuar? [S/N] ').upper()
        if q == 'N' or q == 'S':
            break
    if q == 'N':
        break
lista.sort()
print(30*'-=')
print(f'os numeros digitados foram {lista}')

