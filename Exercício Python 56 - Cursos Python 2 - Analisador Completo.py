print('-=-'*10)
print('   ANALISADOR COMPLETO')
print('-=-'*10)
velho = 0
nomevelho = ''
somaidade = 0
mediaidade = 0
tot20 = 0
for cont in range(1, 5):
    print('----- {}ª PESSOA -----'.format(cont))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ' )).upper().strip()
    somaidade = somaidade + idade
    if cont == 1 and sexo == 'M':
        nomevelho = nome
        velho = idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        tot20 = tot20 + 1

mediaidade = somaidade / 4
print('A média de idade do grupo é: {} anos de idade'.format(mediaidade))
print('O homem mais velho tem {} e o nome dele é {}'.format(velho, nomevelho))
print('O número de mulheres com menos de 20 anos de idade é: {}'.format(tot20))
