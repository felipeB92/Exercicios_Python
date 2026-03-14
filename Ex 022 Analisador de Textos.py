frase = input('digite seu nome completo: ')
div = frase.split()
jun = frase.replace(' ','')
print(frase.upper())
print(frase.lower())
print('seu nome tem {} letras'.format(len(jun)))
print('seu primeiro nome tem {} letras'.format(len(div[0])))

