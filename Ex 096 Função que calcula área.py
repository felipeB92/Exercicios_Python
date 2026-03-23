def area(a,b):
    print(f'a area de um terreno de {a}X{b} é de {a*b}m²')
    print(37 * '-')

print(10*'-','Area do terreno',10*'-')
print(37*'-')
l= float(input('Digite a largura do terreno(m): '))
c= float(input('Digite o comprimento do terreno(m): '))
area(l,c)