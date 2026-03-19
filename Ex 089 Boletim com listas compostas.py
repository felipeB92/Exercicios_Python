from operator import index

lista = []
dados = []
nome = []
notas = []
q = ''
p = 0
while True:
    q = ''
    n= input('nome: ')
    nome.append(n)
    dados.append(nome[:])
    n1 = float(input('nota 01: '))
    notas.append(n1)
    n2 = float(input('nota 02: '))
    notas.append(n2)
    n3 = (n1+n2)/2
    notas.append(n3)
    dados.append(notas[:])
    lista.append(dados[:])
    dados.clear()
    notas.clear()
    nome.clear()
    while q != 'N' and q != 'S':
        q = input('quer continuar? [S/N]:  ').upper()
    if q == 'N':
        break
print('-='*23)
print(f'\033[1mN° Nome{26*' '}Media\033[m')
print('-'*40)
for c in range(0,len(lista)):
    e = list(lista[c][0][0])
    print(f'{c}  {lista[c][0][0]}{(30-len(e))*' '}{lista[c][1][2]}')
while p != 999:
    print('-' * 40)
    p = int(input('mostrar a nota de qual aluno? (999 para sair): '))
    if p == 999:
        print(f'\033[1;31mprograma encerrado\033[m')
        break
    if p > len(lista)-1 or p < 0:
        print(f'\033[31maluno não cadastrado\033[m')
    else:
        print(f' aluno {lista[p][0][0]} notas {lista[p][1][0]}, {lista[p][1][1]}')


