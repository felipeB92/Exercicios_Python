tupla = ("Arroz Branco (5kg)", 29.90, "Feijão Carioca (1kg)", 7.50, "Leite Integral (1L)", 5.40, "Óleo de Soja (900ml)", 6.80, "Açúcar Refinado (1kg)", 4.90, "Café em Pó (500g)", 18.00, "Ovos Brancos (Dúzia)", 12.00)
print(25*'-=')
print(15*'-','tabela de preços', 15*'-')
print(25*'-=')
print(' ')
for c in tupla:
    if tupla.index(c) % 2 == 0:
        print(c,(40-len(c))*'-','R$','{:.2f}'.format(tupla[tupla.index(c)+1]))



