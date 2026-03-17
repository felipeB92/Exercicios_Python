lista =[]
par = []
impar = []
q= ''
while True:
    q = ''
    n= int(input('Digite um valor: '))
    lista.append(n)
    while q != 'S' and q != 'N':
        q = input('Deseja continuar? [S/N]: ').strip().upper()
    if q == 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-=' * 30)
print(f'numeros digitados: {lista}')
print(f'apenas numeros impares: {impar}')
print(f'apenas numeros pares: {par}')