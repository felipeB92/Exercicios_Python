import datetime
a = int(input('digite seu ano de nascimento: '))
b = datetime.date.today().year
c = b - a
if c<18:
     print ('voce precisa se alistar no exercito em {} anos'.format(c) )
elif c>18:
    d = c - 18
    print('voce ja passou {} anos da sua fase de se alistar no exercito'.format(d))
else:
    print('voce esta na fase de se alistar')
