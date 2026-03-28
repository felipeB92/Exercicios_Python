def leiaint():
    while True:
        try:
            n = int(input('digite um numero inteiro: '))
            return n
        except (ValueError, TypeError):
            print('\033[1;31m Por favor digite um numero inteiro\033[m ')
        except KeyboardInterrupt:
            print('\033[1;31m o usuario preferiu não digitar esse numero\033[m')
            return 0

def leiafloat():
    while True:
        try:
            f = (input('digite um numero real:')).replace(',','.')
            n = float(f)
            return n
        except (ValueError, TypeError):
            print('\033[1;31m Por favor digite um numero Real\033[m ')
        except KeyboardInterrupt:
            print('\033[1;31m o usuario preferiu não digitar esse numero\033[m ')
            return 0

try:
    i = leiaint()
    r = leiafloat()
    print(f'o numero inteiro digitado foi {i} e o numero real foi {r} ')
except KeyboardInterrupt:
    print(f'o numero inteiro digitado foi {i} e o numero real foi {r} ')