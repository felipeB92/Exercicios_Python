def leiaint(n):
    while True:
        p = input(n)
        if p.isnumeric():
            print(f'você digitou o numero {p}')
            break
        else:
            print('\033[1;31m Digite um numero inteiro \033[m')

n = leiaint('Digite um numero inteiro: ')