tupla =('macaco',"sol", "livro", "computador", "janela", "correr", "nuvem", "teclado", "porta", "caminho", "vento")
v = ''
a = ''
e = ''
i = ''
o = ''
u = ''
for c in tupla:
    v = list(c)
    if 'a' in v:
        a = v.index('a')
        print(a)
    print(v)
