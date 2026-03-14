v = float(input('digite a velocidade em KM que voce passou em um radar: '))
m = (v-80)*7
if v>= 80:
    print('voce passou acima do limite e foi multado')
    print('valor da sua multa é de {:.2f}'.format(m))
else:
    print('tudo certo sem multas')
