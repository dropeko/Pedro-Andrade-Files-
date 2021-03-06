def leiaInt(mensagem):
    """
    -> Função que verificar se o número foi digitado por extenso
    :param mensagem: Mensagem de erro e solicitado entrada de numero inteiro
    :return: Retorna o valor digitado em números inteiros
    """
    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!! Digite um número inteiro válido!\033[m ')
        if ok:
            break
    return valor


#Programa Principal
print('-=-'*15)
print(f'{"VALIDANDO DADOS":^45}')
print('-=-'*15)
num = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {num}!')
