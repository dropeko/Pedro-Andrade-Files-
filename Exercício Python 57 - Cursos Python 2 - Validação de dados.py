print('-=-'*10)
print('       VALIDAÇÃO DE DADOS')
print('-=-'*10)
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] #Tirando os espaços desnecessários, colocando tudo em maiusculo e selecionando apenas a 1a letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo [M/F]: ')).upper()[0].strip()
print('Sexo {} registrado com sucesso!!'.format(sexo))
