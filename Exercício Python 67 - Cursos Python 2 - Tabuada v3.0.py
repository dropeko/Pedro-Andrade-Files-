print('-=-'*10)
print('          TABUADA V3.0')
print('-=-'*10)
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for contador in range(1, 11):
        produto = num * contador
        print(f'{num} x {contador:2} = {produto}')
print('='*20)
print('!!!!PROGRAMA ENCERRADO!!!!!')
print('='*20)
