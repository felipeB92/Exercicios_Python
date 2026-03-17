lista = []
posicao = 0

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista (posição {len(lista) - 1})')

    else:
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao}')
                break
            posicao += 1
print('-' * 30)
print(f'Os valores digitados em ordem foram: {lista}')