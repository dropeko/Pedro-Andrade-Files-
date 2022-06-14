def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número INTEIRO válido!\033[m ')
            continue
        except(KeyboardInterrupt):
            print(f'\033[0;31mO usuário preferiu não digitar nenhum número\033[m')
            return
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número REAL válido!\033[m ')
            continue
        except(KeyboardInterrupt):
            print(f'\033[0;32mO usuário preferiu não digitar nenhum número\033[m')
            return 0
        else:
            return n



print('-=-'*15)
print(f'{"FUNÇÕES APROFUNDADAS EM Py":^45}')
print('-=-'*15)
numintfora = leiaInt('Digite um número Inteiro: ')
numfloatfora = leiaFloat('Digite um valor Real: ')
print(f'O valor Inteiro digitado foi {numintfora} e o Real foi {numfloatfora}')