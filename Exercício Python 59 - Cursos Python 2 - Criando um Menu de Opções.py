import time
print('-=-'*10)
print('        MENU DE OPÇÕES')
print('-=-'*10)
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
op = 0
while op != 5: # Condição para encerrar o laço
    time.sleep(0.5)
    print('''======================
        OPÇÕES
======================
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA
    ''')
# Estrutura condicional a fim de verificar qual opção o usuário escolheu
    op = int(input('------->> Qual opção?: '))
    if op == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é igual a: {}'.format(num1, num2, soma))
    elif op == 2:
        multi = num1 * num2
        print('A multiplicação entre {} e {} é igual a: {}'.format(num1, num2, multi))
    elif op == 3:
        if num1 > num2:
            print('O maior número digitado foi: {}!'.format(num1))
        else:
            print('O maior número digitado foi: {}!'.format(num2))
    elif op == 4:
        num1 = int(input('Digite o primeiro novo número: '))
        num2 = int(input('Digite o segundo novo número: '))
    elif op == 5:
        print('Finalizando....')
        time.sleep(2)
    else:
        op = int(input('OPÇÃO INVÁLIDA!!! \nSelecione novamente: '))
print('PROGRAMA FINALIZADO!!!!')
