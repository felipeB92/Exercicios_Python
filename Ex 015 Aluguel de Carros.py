d = float(input('quantos dias ficou com o carro: '))
k = float(input('quantos quilometros foram percorridos: '))
t = (d*60)+(k*0.15)
print ('o total a pagar é de R${:.2f}'.format(t))