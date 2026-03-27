import ex111P.moeda.moeda

def metade(num,moeda=False):
    if moeda == True:
        return ex111P.moeda.moeda(num/ 2)
    else:
        return num / 2

def dobro(num,moeda=False):
    if moeda == True:
        return ex111P.moeda.moeda(num*2)
    else:
        return num * 2

def almentar(num,porcentagem,moeda=False):
    if moeda == True:
        p = (num/100 * porcentagem) + num
        return ex111P.moeda.moeda(p)
    else:
        return (num/100 * porcentagem) + num

def diminuir(num,porcentagem,moeda=False):
    if moeda == True:
        return ex111P.moeda.moeda(num - (num/100 * porcentagem))
    return num - (num/100 * porcentagem)