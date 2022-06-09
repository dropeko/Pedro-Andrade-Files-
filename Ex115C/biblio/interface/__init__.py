def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;34mO usuário preferiu não digitar nenhum valor')
            return 0
        else:
            return num


def linha(tamanho = 42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[32m{cont}\033[m - \033[35m{item}\033[m')
        cont = cont + 1
    print(linha())
    opcao = leiaInt('Digite sua opção: ')
    return opcao
