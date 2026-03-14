p = 0
while True:
    p = 0
    n = int(input('qual tabuada deseja ver: '))
    if n <0:
        break
    while True:
        p += 1
        print(f'{n} x {p} = {n*p}')
        if p == 10:
            break
print('fim')