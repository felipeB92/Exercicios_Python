v = float(input('digite o valor do produto: '))
f = int(input('escolha uma forma de pagamento \033[1m1\033[m para dinheiro e \033[1m2\033[m para cartão: '))
if f==2:
    p = float(input('em quantas vezes deseja pagar: '))
    if p==1:
        d = "5% de desconto"
        vd = v/100*5
        t = v-vd
    elif p==2:
        d = "preço normal"
        t = v
    else:
        d= "juros de 20%"
        vd = v/100*20
        t = v+vd
    print('com cartão parcelado em {:.0f}X seu produto vai ficar com {} total de R${:.2f}'.format(p,d,t))
    print('valor por parcela R${:.2f}'.format(t/p))
else:
    vd = v/100*10
    t = v-vd
    print('com pagamento em dinheiro seu produto tem 10% de desconto total de R${:.2f}'.format(t))