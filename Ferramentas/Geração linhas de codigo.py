q = int(input('Quantidade de linhas'))
local = input('Local dos aquivos')
action = input('Nome dos aquivos')

for c in range(0,q):
    print(f'    {local}{action}{c:02}.gif')