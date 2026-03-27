while True:
    n = input('Digite o preço: R$').replace(',','.')
    c = (n.replace(".",""))
    if c.isnumeric():
        b = float(n)
        break
    else:
        print(f'\033[1;31m {n} é um valor invalido\033[m')

print(b)
