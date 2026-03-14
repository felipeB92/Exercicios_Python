s = float(input('digite o valor de seu salario: '))
if s >= 1250:
    b ='10%'
    a = s/100*10+s
else:
    b ="15%"
    a = s/100*15+s
print('seu salario com almento de {} sera de R${}'.format(b,a))