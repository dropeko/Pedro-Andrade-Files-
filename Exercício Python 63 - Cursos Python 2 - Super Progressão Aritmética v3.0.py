print('-=-'*10)
print('   SUPER PROGRESSÃO ARITMÉTICA')
print('-=-'*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
ptermo = termo
totaltermos = 0
maisqtstermos = 10
while maisqtstermos != 0:
    totaltermos = maisqtstermos + totaltermos
    while cont <= totaltermos:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    maisqtstermos = int(input('Quantos termos a mais quer mostrar? [0 para sair]: '))
print('Progressão finalizada com {} termos mostrados'.format(totaltermos))
print('FIM')
