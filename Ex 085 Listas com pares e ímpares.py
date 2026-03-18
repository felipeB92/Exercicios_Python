lista = []
par = []
impar = []
for c in range(0, 7):
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista.append(par)
lista.append(impar)
impar.sort()
par.sort()
print(f'os numeros pares são {lista[0]}' )
print(f'os numeros impares foram {lista[1]}' )