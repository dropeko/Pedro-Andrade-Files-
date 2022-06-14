import random
print('-=-'*10)
print(' JOGO DO PAR OU IMPAR')
print('-=-'*10)
contvit = 0
while True:
    numjog = int(input('Diga um valor: '))
    numcomp = random.randint(0, 10)
    somatotal = numcomp + numjog
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {numjog} e o computador jogou {numcomp}. O total é {somatotal}')
    if parouimpar == 'P':
        if somatotal % 2 == 0:
            contvit = contvit + 1
            print('PARABÉNSS!!! VOCÊ VENCEU!!!')
        else:
            print('O COMPUTADOR VENCEU!!! :(((')
            break
    elif parouimpar == 'I':
        if somatotal % 2 == 1:
            print('PARABÉNSS!!! VOCÊ VENCEU!!!')
            contvit = contvit + 1
        else:
            print('O COMPUTADOR VENCEU!!!! :(((')
            break
    print('Vamos jogar novamente....')
print(f'O número total de vitórias foi: {contvit}')




