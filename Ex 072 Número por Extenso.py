n = 0
t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('digite um numero entre 0 e 20: '))
    if n < 21:
        break
    print('\033[1;31mENTRE 0 e 20\033[m')
print(t[n])