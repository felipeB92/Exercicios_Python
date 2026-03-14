q =''
total = 0
#maior produto
a = ''
#valor
b = 99999999999999999999999999999999999999999999999
c = 0
while True:
    q = ''
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    total += preco
    if preco < b:
        b = preco
        a = produto
    if preco >= 1000:
        c += 1
    while q != 'S' and q != 'N':
        q = input('quer digitar mais produtos[S/N]').upper()
    if q == 'N':
        break
print(f'total da sua compra foi R${total:.2f}')
print(f'o produto mais barato foi o {a} custando R${b:.2f}')
print(f'e {c} produtos custaram mais de R$1000,00')
print('obrigado e volte sempre ')
