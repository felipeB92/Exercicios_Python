n1 = float(input('diga o comprimernto da primeira reta: '))
n2 = float(input('agora a segunda reta: '))
n3 = float(input('agora a terceira reta: '))
list1 = [n1, n2, n3]
list.sort(list1)
if list1[0]+list1[1] > list1[2]:
    print('suas retas são capazes de formar um triangulo')
    if n1==n2==n3:
        t = ('seu Triângulo é Equilátero')
    elif n1==n2 or n1==n3 or n2==n3:
        t =('seu Triângulo é Isósceles')
    else:
        t =('seu Triângulo é Escaleno')
    print(t)
else:
    print('suas retas não são capazes de formar um triangulo')