import datetime
dados = {}
dados['nome'] = str(input('nome: '))
i = int(input('ano de dascimento: '))
dados['idade'] = datetime.date.today().year - i
ct = int(input('nº carteira de trabalho (0 caso não tenha): '))
if ct != 0:
    dados['ctps'] = ct
    ac = int(input('Ano de contratação: '))
    dados['aposentadoria'] = (35 - (datetime.date.today().year - ac)) + (datetime.date.today().year - i)
    dados['salario'] = int(input('salario: R$'))
else:
    dados['ctps'] = 'não tem carteira de trabalho'
print(20*'=-')
for r, v in dados.items():
    print(f'{r} tem o valor {v}')
print(20 * '=-')