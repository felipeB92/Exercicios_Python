n = int(input('digite um valor inteiro: '))
for c in range(1, 11):
    m = (n * c)
    print ('{}X{} = \033[1;31m{}\033[m'.format(n,c,m))