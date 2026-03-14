import math
n = float(input('informe um angulo: '))
r = math.radians(n)
s =math.sin(r)
c =math.cos(r)
t =math.tan(r)
print('o angulo {}° tem seno {:.2f},coseno {:.2f} e tangente {:.2f}'.format(n,s,c,t))

