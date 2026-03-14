a = int(input('escreva um ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('o ano {} é bisexto'.format(a))
else:
    print('o ano {} não é bisexto'.format(a))