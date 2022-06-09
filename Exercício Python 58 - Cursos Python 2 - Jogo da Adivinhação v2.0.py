import random # Importando módulo necessário para randomizar número de 0 a 10
print('-=-'*30)
print('                                  JOGO DA AVINHAÇÃO v2.0')
print('-=-'*30)
print('VOU PENSAR EM UM NÚMERO INTEIRO DE 0 A 10. TENTE ADIVINHAR QUAL É O NÚMERO :B')
print('-'*90)
escolhajogador = int(input('Digite um número inteiro de 0 a 10: ')) # Solicitando entrada ao usuario
escolhacomp = random.randint(0, 10) # Usando a funçao randint para escolher um número de 0 a 10 aleatório
contatentivas = 0 # Contador de tentativas
while not escolhajogador == escolhacomp: # Condição para encerrar o laço de repetição
    contatentivas = contatentivas + 1
    escolhajogador = int(input('Escolheu errado!! Tente novamente!! Digite um número inteiro de 0 a 10: '))
    if escolhajogador < escolhacomp:
        print('Tá pra baixo...')
    else:
        print('Tá pra cima...')
print('PARABÉNS!!!! ATÉ QUE FIM!!! \nO número de tentativas necessárias para acertar foram {} vezes!!'.format(contatentivas))

