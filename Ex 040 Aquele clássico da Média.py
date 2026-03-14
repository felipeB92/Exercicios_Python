n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
v = '\033[1;31m'
a = '\033[1;33m'
ve ='\033[1;32m'
l = '\033[m'
if m <5.0:
    print ('sua media foi de {} infelizmente foi {}reprovado{}'.format(m,v,l))
elif m>=7.0:
    print ('sua media foi de {} parabens foi {}aprovado{}'.format(m,ve,l))
else:
    print ('sua media foi de {} voce ficou de {}recuperação{}'.format(m,a,l))