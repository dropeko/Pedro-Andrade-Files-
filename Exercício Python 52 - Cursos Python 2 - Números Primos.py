print('-=-'*10)
print('        NÚMEROS PRIMOS')
print('-=-'*10)
num = int(input('Digite um número inteiro: '))
print('-=-'*10)
contpar = 0
for cont in range(1, num+1):
    if num % cont == 0:
        print('\033[7;34m{}\033[m'.format(cont))
        contpar = contpar + 1
    else:
        print('{}'.format(cont))
print('-=-'*10)
print('O número {} foi divísivel {} vezes'.format(num, contpar))
if contpar == 2:
    print('E por isso ele é um número PRIMO!')
else:
    print('E por isso ele não é um número PRIMO!')