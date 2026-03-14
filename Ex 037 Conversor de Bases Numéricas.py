n = int(input('digite um numero inteiro: '))
print('escolha uma base de conversão')
t = int(input('sendo \033[1;31m1\033[m = binario, \033[1;31m2\033[m = octual e \033[1;31m3\033[m = hexadecimal: '))
if t == 1:
    numero = bin(n)
    print ('{} em binario é {}'.format(n, numero[2:]))
elif t == 2:
    numero = oct(n)
    print ('{} em octual é {}'.format(n, numero[2:]))
else:
    numero = hex(n)
    print ('{} em hexadecimal é {}'.format(n, numero[2:]))