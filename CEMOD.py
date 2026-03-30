from time import sleep
from xml.dom.minidom import ProcessingInstruction

from cores import *

def leiaInt(r):
    while True:
        try:
            t = int(input(r))
            break
        except ValueError:
            colorir('Digite um valor valido',Estilo.VERMELHONEG)
    return t


def menu():
    print(f'{36*"-"}')
    print(f'{5*' '}BEM VINDO AO BANCO NOJEIRA{5*' '}')
    print(f'{36*"-"}')
    men =['Saldo','Saque','Deposito','Sair']
    p = 1
    for c in men:
        sleep(0.3)
        colorir(f'[{p}] - ',Estilo.NEGRITO,True)
        print(f'{c}')
        p += 1
    print(f'{36 * "-"}')
    q = leiaInt('qual a opcao: ')
    print(f'{36 * "-"}')
    return q

def Saldo(n):
    sleep(0.5)
    print(f'seu saldo atual: R${n}')

def Saque(s):
    v = leiaInt('qual valor deseja sacar:')
    if v > s:
        colorir('Saldo insuficiente',Estilo.VERMELHONEG)
    else:
        sleep(0.5)
        print(f'Realizando saque valor de R${v}')
        s -= v
        contadornotas2(v)
        print('valor sacado com sucesso')
        print(f'novo saldo R${s}')
        return s

def contadornotas2(n):
    notas = [100, 50, 20, 10, 5, 1]
    p = 1
    r = n
    for c in notas:
        if c == 100:
            v = r // c
        else:
            v = r // c
        r -= v * c
        if v != 0:
            sleep(0.5)
            print(f'{v} notas de {c}')

def DEPOSITO(n):
    v = leiaInt('qual valor deseja depositar: \n')
    if v < 0:
        sleep(0.5)
        colorir('valor invalido',Estilo.VERMELHONEG)
    else:
        sleep(0.5)
        colorir(f'Deposito de R${v} Realizado com sucesso',Estilo.VERDE)
        NS = n + v
        sleep(0.5)
        print(f'novo saldo R${NS}')
    return NS