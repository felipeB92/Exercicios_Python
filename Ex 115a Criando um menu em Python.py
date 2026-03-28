def cadastrar(nome, idade):
    try:
        with open("ex115.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome};{idade}\n")
    except Exception as e:
        print(f"Erro ao salvar: {e}")
    else:
        print("Registro salvo com sucesso!")

def listar_pessoas():
    try:
        with open("ex115.txt", "r", encoding="utf-8") as arquivo:
            print("-" * 30)
            print(f"{'NOME':<20}{'IDADE':>3}")
            print("-" * 30)
            for linha in arquivo:
                dado = linha.split(";")
                dado[1] = dado[1].replace("\n", "")
                print(f"{dado[0]:<20}{dado[1]:>3} anos")


    except FileNotFoundError:
        print("Arquivo ainda não existe. Cadastre alguém primeiro!")

o = 0

while True:
    if o == 3:
        break
    o = 0
    print(30*"-")
    print('        MENU PRINCIPAL ')
    print(30*"-")
    print('\033[33m1 - \033[mCadastrar Pessoa')
    print('\033[33m2 - \033[mListar Pessoas')
    print('\033[33m3 - \033[mSair do sistema')
    while o != 1 and o != 2 and o != 3:
        try:
            print(30*"-")
            o = int(input('selecioneuma opção: '))
            if o == 1:
                print(30*'-')
                print("      Cadastrar Pessoa")
                print(30*'-')
                N = input('Nome: ')
                I = input('Idade: ')
                cadastrar(N , I)
            if o == 2:
                print(30*'-')
                print("      PESSOAS CADASTRADAS")
                print(30*'-')
                listar_pessoas()
            if o == 3:
                break
        except:
            print('\033[1;31m  OPÇãO INVALIDA \033[m')
print(30*'-')
print("               \033[34mFIM\033[m")
print(30*'-')
