import datetime
i = int(input('digiteo ano de nascimento do atleta: '))
a = datetime.date.today().year
b = a-i
if b<=9:
    print('o atleta tem {} anos e esta na categoria mirim'.format(b))
elif b<=14:
    print('o atleta tem {} anos e esta na categoria infantil'.format(b))
elif b<=19:
    print('o atleta tem {} anos e esta na categoria junior'.format(b))
elif b==20:
    print('o atleta tem {} anos e esta na categoria senior'.format(b))
else:
    print('o atleta tem {} anos e esta na categoria master'.format(b))

