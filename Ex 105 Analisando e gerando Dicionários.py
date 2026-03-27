def notas(a,sit=False):
    maior = 0
    menor = 0
    total = 0
    soma = 0
    N ={}
    for c in range(0, len(a)):
        total += 1
        soma +=a[c]
        if c == 0:
            menor = a[c]
            maior = a[c]
        else:
            if a[c] > maior:
                maior = a[c]
            if a[c] < menor:
                menor = a[c]
    N['total'] = total
    N['maior'] = maior
    N['menor'] = menor
    N['media'] = (soma/len(a))
    if sit == True:
        if N['media'] >= 7:
            N['situação'] = 'boa'
        elif N['media'] <= 5:
            N['situação'] = 'Ruim'
        else:
            N['situação'] = 'razoável'
    print(N)


lista=[]

while True:
    q= ''
    r = float(input('Digite a nota de um aluno: ' ))
    lista.append(r)
    while q !='S' and q !='N':
        q = input('Quer inserir mais notas? [S/N]: ').upper()
    if q == 'N':
        break
S = ''
while S !='S' and S !='N':
    S = input('deseja ver a situação? [S/N]: ').upper()
if S == 'N':
    S = False
else:
    S = True

notas(lista,sit=S)
print(f'as notas foram {lista}')
