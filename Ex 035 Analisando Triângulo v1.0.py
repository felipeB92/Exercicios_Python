a = float(input('digite o comprimento da primeira reta: '))
b = float(input('agora a segunda reta: '))
c =float(input('e por fim a terceira reta: '))
list1 = [a,b,c]
list2 = sorted(list1)
if list2[0] + list2[1] > list2[2]:
    print('suas tres retas são capazes de formar um triangulo')
else:
    print('suas retats não formam um triangulo')