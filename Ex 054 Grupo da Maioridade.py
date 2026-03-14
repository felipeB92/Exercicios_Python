a = 0
for c in range(0,7):
    n = int(input('digite a idade de uma pessoa: '))
    if n >= 18:
        a += 1
c = 7-a
print ('{} pessoas são maiores de idade e {} são menores de idade'.format(a,c))
