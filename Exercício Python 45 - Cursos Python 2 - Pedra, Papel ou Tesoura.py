import random
print('-=-'*10)
print('   PEDRA, PAPEL OU TESOURA')
print('-=-'*10)
print('Suas opções: \n [ 0 ] PEDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA')
# Solicitando a entrada de dados ao usuario
opjog = int(input('Escolha: '))
# Definindo a lista para o receber o valor do jogador e do computador
lista = ['Pedra', 'Papel', 'Tesoura']
# Randomizando a escolha do computador
opcomp = random.randint(0, 2)
print('-=-'*10)
# Imprimindo na tela a escolha do jogador e do computador
print('O computador jogou: {}'.format(lista[opcomp]))
print('O jogador jogou: {}'.format(lista[opjog]))
print('-=-'*10)
# Estrutura condicional a fim de verificar quem foi o vencedor
if opcomp == 0: # Computador jogou PEDRA
    if opjog == 0:
        print('JOGADA EMPATOU!')
    elif opjog == 1:
        print('O jogador ganhou!!')
    elif opjog == 3:
        print('O computador ganhou!!')

elif opcomp == 1: # Computador jogou PAPEL
    if opjog == 0:
        print('O computador venceu!!')
    elif opjog == 1:
        print('JOGADA EMPATOU!!')
    elif opjog == 2:
        print('O jogador venceu!!')

elif opcomp == 2: # Computador jogou TESOURA
    if opjog == 0:
        print('O jogador venceu!!')
    elif opjog == 1:
        print('O computador venceu!!')
    elif opjog == 2:
        print('JOGADA EMPATADA!!')


