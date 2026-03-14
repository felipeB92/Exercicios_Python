nove = 0
tupla = ()
pares =()
p = 0
for c in range(0, 4):
    n=int(input(f'digite o {c+1}º numero: '))
    tupla += (n,)
    if n == 9:
        nove += 1
    if n % 2 == 0:
        pares += (n,)
        p += 1
print (f'o numero 9 apareceu {nove} vezes')
if 3 in tupla:
    print(f'o numero 3 apareceu primeiro na {tupla.index(3)+1}º posição')
else:
    print('não foi digitado o numero 3')
if p > 0:
    print(f'os numeros pares foram {pares}')
else:
    print('não houveram numeros pares')