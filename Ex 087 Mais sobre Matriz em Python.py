list1 = []
base = []
somapar = 0
maior2 = 0
soma3 = 0

for c in range(0, 3):
    n = int(input(f'digite um valor para [0 ,{c}]:'))
    base.append(n)
    list1.append(base[:])
    base.clear()
for c in range(0, 3):
    n = int(input(f'digite um valor para [1 ,{c}]:'))
    base.append(n)
    list1.append(base[:])
    base.clear()
for c in range(0, 3):
    n = int(input(f'digite um valor para [2 ,{c}]:'))
    base.append(n)
    list1.append(base[:])
    base.clear()
print ('-='*30)
print (f'[  {list1[0][0]}  ]   [  {list1[1][0]}  ]  [ {list1[2][0]}  ]')
print (f'[  {list1[3][0]}  ]   [  {list1[4][0]}  ]  [ {list1[5][0]}  ]')
print (f'[  {list1[6][0]}  ]   [  {list1[7][0]}  ]  [ {list1[8][0]}  ]')
print('-='*30)

for v,c in enumerate(list1):
    if list1[v][0] % 2 == 0:
        somapar += list1[v][0]
for c in range(3,6):
    if list1[c][0] > maior2:
        maior2 = list1[c][0]

for c in range(2,9,3):
    soma3 += list1[c][0]

print(f'a soma dos valores pares é {somapar}')
print(f'o maior valor da segunda linha é {maior2}')
print(f'e a soma dos valores da terceira coluna é {soma3}')

print('-='*30)