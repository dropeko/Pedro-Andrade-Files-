print('-=-'*10)
print('     PROGRESSÃO ARITMÉTICA')
print('-=-'*10)
ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Agora insira a razão: '))
cont = 1
termo = ptermo
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('FIM!')
