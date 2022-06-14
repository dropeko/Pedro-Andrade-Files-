print('-=-'*10)
print('         FATORIAL')
print('-=-'*10)
num = int(input('Digite o número para verificar seu fatorial: '))
cont = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial = fatorial * cont
    cont = cont - 1
print('{}'.format(fatorial))
