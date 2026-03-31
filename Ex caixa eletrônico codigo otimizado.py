from CEMOD import *
print('em processo digite',)
print('\033[1;32mconta 0 senha 123\033[m ou',end=' ')
print('\033[1;32mconta 1 senha 321\033[m')
dados = "cadastros.json"
lista = carregar_dados(dados)

Con = int(login())
if Con == 999:
    print('Encerrando')
else:
    saldo = int(lista[Con]['saldo'])
    q = 0
    select(q,saldo)
print('obrigado por ultilizar o banco nojeira')