def escreva(txt):
    tam = int(len(txt))
    print('~'*(tam+4))
    print(f'  {txt}  ')
    print('~'*(tam+4))

t = input('Digite algo: ')
escreva(t)