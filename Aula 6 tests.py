from cores import *
def menu():
    print('BEM VINDO AO BANCO NOJEIRA':^'-')
    men =['Saldo','Saque','Deposito','Sair']
    p = 1
    for c in men:
        colorir(f'[{p}] - ',Estilo.NEGRITO,True)
        print(f'{c}')
        p += 1

menu()