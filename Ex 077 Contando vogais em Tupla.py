tupla =('macaco',"sol", "livro", "computador", "janela", "correr", "nuvem", "teclado", "porta", "caminho", "vento")
for c in tupla:
    print(f'\n na palavra \033[1m{c}\033[m temos as vogais:', end=' ')
    for l in c:
        if l in 'aeiou':
            print(l, end=' ')
