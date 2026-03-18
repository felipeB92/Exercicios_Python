list1 = []
base = []

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
print('-='*30)
print (f'[  {list1[0][0]}  ]   [  {list1[1][0]}  ]  [ {list1[2][0]}  ]')
print (f'[  {list1[3][0]}  ]   [  {list1[4][0]}  ]  [ {list1[5][0]}  ]')
print (f'[  {list1[6][0]}  ]   [  {list1[7][0]}  ]  [ {list1[8][0]}  ]')
print('-='*30)
