s = 0
while s != 'F' and s != 'M':
    s=str(input("Digite seu sexo: ")).upper()
    if s != 'M' and s != 'F':
        print('\033[1;31mdigite corretamente M ou F\033[m')
