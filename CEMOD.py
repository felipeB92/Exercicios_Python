from time import sleep
from cores import *
import json


def carregar_dados(nome_arquivo):
    """Lê o arquivo JSON e retorna a lista de dicionários."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver vazio, retorna lista vazia
        return []

def salvar_dados(nome_arquivo, lista_dicionarios):
    """Salva a lista de dicionários no formato JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # indent=4 deixa o arquivo legível para humanos
            json.dump(lista_dicionarios, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar: {e}")
        return False

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
    print(f'{15*' '}MENU')
    print(f'{36*"-"}')
    men =['Saldo','Saque','Deposito','Sair']
    p = 1
    for c in men:
        sleep(0.3)
        colorir(f'[{p}] - ',Estilo.NEGRITO,True)
        print(f'{c}')
        p += 1
    print(f'{36 * "-"}')
    q = leiaInt('Selecione uma opcao: ')
    print(f'{36 * "-"}')
    return q

def select(q,saldo):
    while q != 4:
        q = menu()
        if q == 1:
            r = Saldo(saldo)
        elif q == 2:
            r = saldo = Saque(saldo)
        elif q == 3:
            r = saldo = DEPOSITO(saldo)
        elif q == 4:
            print('operaçao finalizada')
            return saldo
        else:
            sleep(0.5)
            print('\033[1;31m opção invalida\033[m')
    return r

def Saldo(n):
    sleep(0.5)
    print(f'seu saldo atual: R${n}')

def Saque(s):
    v = leiaInt('qual valor deseja sacar:')
    if v > s:
        print('\033[1;31m   Saldo insuficiente\033[m')
    elif v < 0:
        print('\033[1;31m   Valor Invalido\033[m')
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
        NS = n
    else:
        sleep(0.5)
        colorir(f'Deposito de R${v} Realizado com sucesso',Estilo.VERDE)
        NS = n + v
        sleep(0.5)
        print(f'novo saldo R${NS}')
    return NS

def login():
    print(f'{36*"-"}')
    print(f'{5*' '}BEM VINDO AO BANCO NOJEIRA{5*' '}')
    print(f'{36*"-"}')
    print('digite sua conta e senha ou \n0 em conta para cadastrar nova conta')
    print()
    b = 0
    dados = "cadastros.json"
    lista = carregar_dados(dados)
    while True:
        c=leiaInt('\033[1mNumero da conta\033[m: ')
        if c > (len(lista)-1) or c < 0:
            print('\033[1;31m   CONTA INVALIDA \033[m')
        elif c == 0:
            cadastro()
            return 0
        else:
            print(f'NOME:{lista[c]['nome']}')
            senha = leiaInt('\033[1mDigite sua senha:\033[m ')
            if senha == (lista[c]['senha']):
                print(f'\033[1;32m    Entrando\033[m')
                return c
            else:
                print('\033[1;31m   Senha incorreta\033[m')
                b +=1
                print(f'\033[1;31m Tentativa {b}/3\033[m')
                if b == 3:
                    print(f'\033[1;31m Cartão Bloqueado')
                    return 999

def cadastro():
    dados = "cadastros.json"
    lista = carregar_dados(dados)
    temp = {}
    print(f'{40*"-"}')
    print(f'{10*" "}CADASTRO NOVA CONTA')
    print(f'{40*"-"}')
    temp['nome'] = input('Nome: ').upper()
    temp['senha'] = leiaInt('Senha: ')
    temp['saldo'] = leiaInt('valor do deposito inicial : R$')
    lista.append(temp)
    salvar_dados("cadastros.json",lista)
    print(f'numero da sua conta é \033[1;32m{len(lista)-1}\033[m')
    return 0










