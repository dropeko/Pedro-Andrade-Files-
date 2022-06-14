print('-=-'*10)
print('  VÁRIOS NÚMEROS COM FLAG')
print('-=-'*10)
contnum = 0
soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma = soma + num
    contnum = contnum + 1
print(f'Foram {contnum} números digitados e a soma entre eles é: {soma}')