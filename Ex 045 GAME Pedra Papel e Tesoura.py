import random

from django.template.defaultfilters import lower

p = str(input(' escolha entre pedra papel ou tesoura: '))
lista = ['pedra','papel','tesoura']
c = random.choice(lista)
pp =lower(p)
if pp == "pedra" and c == 'papel':
    v = "perdeu"
elif pp == "pedra" and c == 'tesoura':
    v = "ganhou"
elif pp == 'papel' and c == 'pedra':
    v = 'ganhou'
elif pp == 'papel' and c == 'tesoura':
    v = 'perdeu'
elif pp == 'tesoura' and c == 'pedra':
    v = 'perdeu'
elif pp == 'tesoura' and c == 'papel':
    v = 'ganhou'
elif pp == c:
    v = 'empatou'
else:
    v = 'perdeu'
    print('\033[1;31mvoce trapaceou\033[m')
print('eu escolhi {} e voce {} voce {}'.format(c,pp,v))

