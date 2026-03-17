lista =[]
q = ''
cont = 0
while True:
    if q == 'N':
        break
    else:
        q = ''
    n = int(input('Digite um numero: '))
    lista.append(n)
    cont += 1
    while q != 'S' and q!= 'N':
        q = input('Quer continuar? [S/N] ').upper()
lista.sort(reverse=True)
print(lista)
print('-=' * 30)
print(f'foram digitados {cont} numeros ' )
if 5 in lista:
    print(f'foi digitado o numero 5')
else:
    print('não foi digitado o numero 5')
print (f'os numeros em ordem decresentes são {lista}')