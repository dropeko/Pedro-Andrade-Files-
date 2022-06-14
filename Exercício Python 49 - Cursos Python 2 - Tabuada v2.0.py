print('-=-' * 10)
print('       TABUADA')
print('-=-' * 10)
num = int(input('Digite um número inteiro para ver sua tabuada: '))
for cont in range(1, 11):
    result = num * cont
    print('{} x {:2} = {}'.format(num, cont, result))


