import datetime
def voto(a):
    i = (datetime.date.today().year) - a
    if  i >= 18:
        b = 'é Obrigatorio'
    if i >= 65:
        b = 'não é opcional'
    if i < 18:
        b = 'não é nescessario'
    print(f'com {i} anos o voto {b}')

n = int(input('em que ano você nasceu?: '))
voto(n)


