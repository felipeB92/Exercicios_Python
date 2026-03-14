v =int(input('informe a distancia em Km da sua viagem: '))
if v >= 200:
    p1 = v*0.45
else:
    p1 = v*0.50
print('o valor da sua viagen é de R${:.2f}'.format(p1))


