import math
n1=float(input('valor 1: '))
n2=float(input('valor 2: '))
n3=[n1,n2]
o =(4)
while o==4:
    print('escolha uma das opções abaixo')
    print('[1]somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novo')
    print('[5]sair')
    o = int(input(':'))
    if o==1:
        r= sum(n3)
    elif o==2:
        r=math.prod(n3)
    elif o==3:
        n4 = list(n3)
        list.sort(n4)
        r=n4[-1]
    elif o==4:
        p=float(input('digite o novo valor: '))
        n3.append(p)
    elif o == 5:
        print('operação finalizada')
    else:
        print('opção invalida')
if o >= 5 or o == 0:
    print('fim')
else:
    print('o resultado é {} '.format(r) )


