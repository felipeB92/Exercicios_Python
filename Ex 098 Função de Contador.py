import time
def contador(a, b, c):
    if c >= 0:
        b += 1
        print(f'contagem de {a} até {b-1} de {c} em {c}')
    if c < 0:
        b -= 1
        print(f'contagem de {a} até {b+1} de {c-(c*2)} em {c-(c*2)}')
    print('-'*40)
    for c in range(a, b, c):
        time.sleep(0.5)
        print(f'{c} ', end='')
    print(f'\n{'-' * 40}')


inicio = 1
fim = 10
passo = 1
contador(inicio, fim, passo)

inicio = 10
fim = 0
passo = -2
contador(inicio, fim, passo)

inicio = int(input('digite o inicio da contagem: '))
fim = int(input('digite o fim da contagem: '))
passo = int(input('digite o passo da contagem: '))
if passo == 0:
    passo = 1
contador(inicio, fim, passo)
