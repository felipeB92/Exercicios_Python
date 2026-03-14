s = ''
t = 0
h = 0
m = 0
while True:
    s =''
    i = int(input('Idade: '))
    while s != 'M' and s!= 'F':
        s = input('Sexo [M/F]: ').upper()
    if i >=18:
        t += 1
    if s == 'M':
        h += 1
    if s == 'F' and i >=20:
        m += 1
    p = ''
    while p != 'S' and p != 'N':
        p = input('Quer continuar? [S/N]: ').upper()
    if p == 'N':
        break
print(f'total de pessoas com mais de 18 anos é {t}')
print(f'total de homens foi {h}')
print(f'e {m} mulheres com mais de 20 anos')
print('FIM DO PROGRAMA')

