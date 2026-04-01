from CEMOD import *
print('em processo digite',)
print('\033[1;32mconta 1 senha 123\033[m ou',end=' ')
print('\033[1;32mconta 2 senha 321\033[m')

dados = "cadastros.json"
lista = carregar_dados(dados)

Con = int(login())
if Con == 999:
    print('Encerrando')
elif Con == 0:
    print('\033[1;32m Conta cadastrada com sucesso\033[m')
else:
    saldo = lista[Con]['saldo']
    q = 0
    resto = int(select(q,saldo))
    lista[Con]['saldo'] = resto
    salvar_dados("cadastros.json", lista)
print('obrigado por ultilizar o banco nojeira')