print('-=-'*10)
print('  ANALISE DE DADOS DE UM GRUPO')
print('-=-'*10)
qtdmaioridade = 0
qtdhomem = 0
qtdademu20 = 0

while True:
    print('-'*30)
    print('   CADASTRE UM PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        qtdmaioridade = qtdmaioridade + 1
    if sexo == 'M':
        qtdhomem = qtdhomem + 1
    if sexo == 'F':
        if idade < 20:
            qtdademu20 = qtdademu20 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos é: {qtdmaioridade}')
print(f'A quantidade de homens cadastrados foi: {qtdhomem}')
print(f'A quantidade de mulheres com menos de 20 anos é: {qtdademu20}')
print('ACABOU!! ')
