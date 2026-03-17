e = input('digite uma expressão matematica: ')
lista = list(e)
a = 0
b = 0
for c in lista:
    if c == '(':
        a += 1
    if c == ')':
        b += 1
if a == b:
    print('\033[1;32mSua expressão esta correta\033[m')
else:
    print('\033[1;31mSua expressão esta errada\033[m')