f = input("Digite uma frase: ")
l = f.lower()
a = l.replace(' ', '')
b = list(a)
b.reverse()
c = list(a)
if b == c:
    print('sua frase é um palindromo!')
else:
    print('sua frase \033[1;31mnão\033[m é um palindromo!')



