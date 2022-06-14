print('-=-'*10)
print('  SEQUENCIA DE FIBONACCI')
print('-=-'*10)
qtdtermos = int(input('Digite quantos termos da sequencia de fibonacci você quer: '))
cont = 3
termo1 = 0
termo2 = 1
print('{} -> {}'.format(termo1, termo2), end='')
while cont < qtdtermos:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont = cont + 1