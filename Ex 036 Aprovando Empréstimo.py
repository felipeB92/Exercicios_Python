c =float(input('qual o valor do imovel que ira adiquirir: '))
s =float(input('qual valor do seu salario: '))
a =float(input('em quantos anos pretende quitar o emprestimo: '))
p = a*12
vp = c/p
t = (s/100)*30
n = '\033[1m'
l = '\033[m'
print('seu salario é de {} R${:.2f}{}'.format(n,s,l))
print('seu imovel custara {}R${:.2f}{} parcelado em {}{:.0f} vezes{} de {}R${:.2f}{}'.format(n,c,l,n,p,l,n,vp,l))
if t >= vp:
    print('seu imprestimo foi \033[1;32;40maprovado\033[m')
else:
    print('seu imprestimo foi \033[1;30;41mReprovado\033[m')