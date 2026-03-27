import time
def ajuda():
    while True:
        q = input(' função ou biblioteca: ')
        if q.upper() == 'FIM':
            break
        else:
            print(' ')
            time.sleep(0.5)
            print(f'\033[1;34m{(len(q)+34)*'-'}')
            time.sleep(0.5)
            print(f'  Acessando o manual do comando {q} ')
            time.sleep(0.5)
            print(f'{(len(q) + 34) * '-'}')
            print(f'\033[1;30;42m')
            time.sleep(0.5)
            help(q)
            print('\033[m')
            print(f'{(30)*'-'}')



print('')
print(f'\033[1;30;44m{30*'-'}')
print('   SISTEMA DE AJUDA PYHELP')
print(30*'-')
print('\033[m')

ajuda()

print(30*'-')
print('Obrigado por utilizar o PYHELP')
print('        até breve')
print(30*'-')

