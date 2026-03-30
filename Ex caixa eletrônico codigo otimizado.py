from CEMOD import *
from time import sleep

saldo = 1000
q = 0

while q != 4:
    q = menu()
    if q == 1:
        Saldo(saldo)
    elif q == 2:
            saldo = Saque(saldo)
    elif q == 3:
        saldo = DEPOSITO(saldo)
    elif q == 4:
        print('operaçao finalizada')
    else:
        sleep(0.5)
        print('\033[1;31m opção invalida\033[m')
print('obrigado por ultilizar o banco nojeira')