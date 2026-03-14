import math
n1 =int(input('primeiro numero: '))
n2 =int(input('segundo numero: '))
n3 =int(input('terceito numero: '))
list = [n1, n2, n3]
r = sorted(list)
print ('o maior numero é {} e o menor é {}'.format(r[-1],r[0]))