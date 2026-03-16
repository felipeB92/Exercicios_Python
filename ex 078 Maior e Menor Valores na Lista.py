lista = []
i = 0
t = 0
menor = 99999999
maior = 0
for c in range(0,5):
    n = int(input(f'digite o {c+1}º numero: '))
    lista.append(n)
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'o menor numero foi {menor} e o maior foi {maior}')
print(f'o numero {maior} apareceu nas posições',end= ' ')
for c in lista :
    if maior in lista[i:]:
        print(lista.index(maior,i)+1,end=' ')
        i = lista.index(maior,i)+ 1
print(f'\no numero {menor} apareceu nas posições',end= ' ')
for c in lista :
    if menor in lista[t:]:
        print(lista.index(menor, t) + 1, end=' ')
        t = lista.index(menor, t) + 1




