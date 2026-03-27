import ex107m

def metade(num,moeda=False):
    if moeda == True:
        return ex107m.moeda(num/ 2)
    else:
        return num / 2

def dobro(num,moeda=False):
    if moeda == True:
        return ex107m.moeda(num*2)
    else:
        return num * 2

def almentar(num,porcentagem,moeda=False):
    if moeda == True:
        p = (num/100 * porcentagem) + num
        return ex107m.moeda(p)
    else:
        return (num/100 * porcentagem) + num

def diminuir(num,porcentagem,moeda=False):
    if moeda == True:
        return ex107m.moeda(num - (num/100 * porcentagem))
    return num - (num/100 * porcentagem)

def moeda(num,moeda=False):
    return (f'R${num:.2f}')


def resumo(a,b,c):
    print(30 * '_')
    print(f'{8 * ' '}RESUMO DO VALOR{8 * ' '}')
    print(30 * '_')
    print(f'Preço Analizado{7 * ' '}{a}')
    print(f'Dobro do preço{8 * ' '}{ex107m.dobro(a,True)}')
    print(f'Metade do preço{7 * ' '}{ex107m.metade(a,True)}')
    print(f'80% de almento{8 * ' '}{ex107m.almentar(a,b,True)}')
    print(f'35% de redução{8 * ' '}{ex107m.diminuir(a,c,True)}')
    print(30 * '_')


