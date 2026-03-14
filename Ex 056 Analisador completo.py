ti = 0
tm = 0
list =[]
for c in range(1,5):
    print('\033[1;31mpessoa {}\033[m:'.format(c))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    id= str('{:03d}'.format(i))
    sexo = str(input('Sexo(F/M): '))
    se= sexo.upper()
    ti += i
    if se == 'F' and i <20:
        tm += 1
    elif se == 'M':
        lc=[id,n]
        lj="".join(lc)
        list.append(lj)
list.sort()
media = (ti/4)
print('A media de idades do grupo é {} e {} mulher(es) tem menos de 20 anos e o homem mais velho é {} com {} anos '.format(media, tm,list[-1][3:],list[-1][:3]))