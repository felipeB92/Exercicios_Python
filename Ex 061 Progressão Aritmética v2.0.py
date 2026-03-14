n = int(input('informe o primeiro numero: '))
p = int(input('infome a Progressão Aritmética (PA): '))
a = 0
b = 0
while a!=10:
    if a == 0:
        b += n
    else:
        b += p
    a += 1
    print(b)
print('fim')