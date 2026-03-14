import math
co =float(input('digite o compriment do cateto oposto: '))
ca = float(input('agora do cateto adjacente: '))
h = math.pow(co,2)+math.pow(ca,2)
r = math.sqrt(h)
print ('a ipotenusa é igual a {}'.format(r))
