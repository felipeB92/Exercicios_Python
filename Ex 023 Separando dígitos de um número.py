n = str(input('digite um numero entre 0 e 9999: '))
n2 =(len(n))
n3 = int(4-n2)
n4 = n3*"*"
n5 = n4+n
print ('milhar:{}'.format(n5[0]))
print ('centena:{}'.format(n5[1]))
print ('dezena:{}'.format(n5[2]))
print ('unidade:{}'.format(n5[3]))
