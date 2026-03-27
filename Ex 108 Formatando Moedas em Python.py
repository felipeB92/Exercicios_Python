import ex107m

n = float(input('digite o preço: R$'))
print(f'A metade de {ex107m.moeda(n)} é {ex107m.moeda(ex107m.metade(n))}')
print(f'O dobro de {ex107m.moeda(n)}é {ex107m.moeda(ex107m.dobro(n))}')
print(f'Almento de 10% em {ex107m.moeda(n)} é {ex107m.moeda(ex107m.almentar(n,10))}')
print(f'reduziondo 13% de {ex107m.moeda(n)} é {ex107m.moeda(ex107m.diminuir(n,13))}')