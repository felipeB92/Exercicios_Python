print('digite 999 para parar')
s = 0
t = 0
n = 0
while True:
    n= int(input('digite um numero: '))
    if n == 999:
            break
    s += n
    t += 1
print(f'a soma dos {t} numeros foi {s}')