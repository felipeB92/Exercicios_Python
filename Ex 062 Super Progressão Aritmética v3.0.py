n = int(input('informe o primeiro numero: '))
p = int(input('infome a Progressão Aritmética (PA): '))
a = 0
b = 0
t = 1
while a!=10:
    if a == 0:
        b += n
    else:
        b += p
    a += 1
    print(b)
while t != 0:
    t = int(input('quer continuar quantos numeros? digite 0 para parar: '))
    for c in range(0,t):
        b += p
        a += 1
        print(b)

print('fim')