p = float(input('digite seu peso: '))
a = float(input('digite sua altura: '))
imc = p/(a*a)
if imc < 18.5:
    print('seu IMC é de {:.2f}:abaixo do peso'.format(imc))
elif imc <= 25:
    print('seu IMC é de {:.2f}:peso ideal'.format(imc))
elif imc <= 30:
    print('seu IMC é de {:.2f}:sobrpeso'.format(imc))
elif imc <= 40:
    print('seu IMC é de {:.2f}:Obesidade'.format(imc))
else:
    print('seu IMC é de {:.2f}:Obesidade morbida'.format(imc))