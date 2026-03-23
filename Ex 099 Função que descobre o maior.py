def maior(num):
    cont=0
    mai = 0
    print(30*'-')
    for c in range(0,len(num)):
        cont += 1
        if mai == 0:
            mai = num[c]
        else:
            if num[c] > mai:
                mai = num[c]
    print(f'{num} foram digitados {cont} numeros ')
    print(f'o maior numero foi {mai}')
    print(30*'-')

r = ''
lista = []
while True:
    r = ''
    num = int(input('digite um numero: '))
    lista.append(num)
    while r != 'S' and r != 'N':
        r = input('deseja digitar mais numeros ? [S/N]: ').upper()
    if r == 'N':
        break
maior(lista)





