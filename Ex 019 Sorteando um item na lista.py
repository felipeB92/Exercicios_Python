import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('nome do segundo aluno: ')
a3 = input('nome do terceiro aluno: ')
a4 = input('nome do quarto aluno: ')
lista = [a1,a2,a3,a4]
E = random.choice (lista)
print('o escolhido foi {}!'.format(E))
