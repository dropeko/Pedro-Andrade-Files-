print('-=-'*10)
print('    TRATANDO VARIOS NUMEROS')
print('-=-'*10)
num = int(input('Digite um numero inteiro: '))
soma = 0
contnum = 0
while num != 999:
    soma = soma + num
    contnum = contnum + 1
    num = int(input('Digite outro número inteiro: '))
print('A soma de todos os valores foi: {} \nA quantidade de números digitados foi: {}'.format(soma, contnum))
