lista =[]
for c in range(0,5):
    p = int(input('digite o peso da {}º pessoa em Kg: '.format(c+1)))
    lista.append(p)
l = sorted(lista)
print ('o maior peso foi de {} Kg e o menor foi {} Kg'.format(l[-1],l[0]))