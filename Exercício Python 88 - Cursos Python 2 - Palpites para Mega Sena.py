import random, time
print('-=-'*15)
print('          PALPITES PARA MEGA SENA')
print('-=-'*15)
lista = list()
jogos = list()
qtsjogos = int(input('Quantos jogos você quer sortear?: '))
totjogos = 1
while totjogos <= qtsjogos:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totjogos = totjogos + 1
print('-=-'*3, f'SORTEANDO {qtsjogos} JOGOS', '-=-'*3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}')
    time.sleep(1)
print('--------- BOA SORTE ---------')
