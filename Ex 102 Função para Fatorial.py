def fatorial(n):
    c = n-1
    f = n
    while c > 0:
        f = f * c
        c -= 1
    print(f)
    if p == 'S':
        c = n
        print(n,end=' ')
        while c > 1:
            c -= 1
            print(f'X {c}', end=' ')
        print(f'= {f}')
p =''
k =int(input('qual numero deseja ver o fatorial?: '))
while p != 'S' and p != 'N':
    p = input('deseja ver o calculo?:[S/N]: ').upper()
fatorial(k)
