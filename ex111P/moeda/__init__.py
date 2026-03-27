from ex111P.dado import dado

def moeda(num,moeda=False):
    return (f'R${num:.2f}')


def resumo(a,b,c):
    print(30 * '_')
    print(f'{8 * ' '}RESUMO DO VALOR{8 * ' '}')
    print(30 * '_')
    print(f'Preço Analizado{7 * ' '}{moeda(a)}')
    print(f'Dobro do preço{8 * ' '}{dado.dobro(a,True)}')
    print(f'Metade do preço{7 * ' '}{dado.metade(a,True)}')
    print(f'80% de almento{8 * ' '}{dado.almentar(a,b,True)}')
    print(f'35% de redução{8 * ' '}{dado.diminuir(a,c,True)}')
    print(30 * '_')
