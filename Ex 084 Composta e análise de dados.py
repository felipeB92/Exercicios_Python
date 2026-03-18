lista =[]
dados =[]
maior = 0
menor = 0
cont = 0
while True:
    q = ''
    n = input('Nome: ')
    dados.append(n)
    p = int(input('peso em Kg: '))
    dados.append(p)
    lista.append(dados[:])
    while q !='N' and q !='S':
        q = input('Deseja continuar? [S/N]').upper()
        if q == 'N':
            break
        if q == 'S':
            dados.clear()
    if q == 'N':
        break
for c in lista:
    if menor == 0:
        menor = c[1]
        maior = c[1]
    if c[1] > maior:
        maior = c[1]
    if c[1] < menor:
        menor = c[1]
    cont += 1
print('-='*30)
print(f'foram cadastradas {cont} pessoas')
print()
print (f'o maior peso foi {maior} Kg de ',end=' ')
for c in lista:
    if c[1] == maior:
        print(f'{c[0]} ',end='-')
print('\n')
print(f'o menor peso foi {menor} Kg de ', end='')
for c in lista:
    if c[1] == menor:
        print(f'{c[0]} ', end='-')
print('\n')
print('-='*30)