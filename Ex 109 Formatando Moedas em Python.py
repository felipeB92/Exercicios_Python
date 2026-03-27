from pickle import TRUE

import ex107m
n = float(input('digite o preço: R$'))
print(f'A metade do valor é {ex107m.metade(n,True)}')
print(f'O dobro do valor é {ex107m.dobro(n,True)}')
print(f'Almento de 10% temos {ex107m.almentar(n,10,True)}')
print(f'reduziondo 13% temos {ex107m.diminuir(n,13,True)}')