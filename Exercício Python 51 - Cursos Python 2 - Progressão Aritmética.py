import math
print('-=-' * 10)
print('   PROGRESSÃO ARITMÉTICA')
print('-=-' * 10)
# Solicitando a entrada de dados ao usuário
termo = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
# Fórmula do Enésimo termo de uma PA
dec = termo + (10 - 1) * raz
# Estrutura em Laço For a fim de realizar a progressão aritmética dos 10 primeiros termos
for cont in range(termo, dec + raz, raz):
    print('{} '.format(cont), end='-> ')
print('ACABOU!')



