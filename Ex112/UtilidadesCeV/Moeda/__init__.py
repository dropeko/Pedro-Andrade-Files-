#Arquivo armanzenando as funções que serão utilizadas nos exercicios 107 a 112
#Funções aumentar, diminuir, dobro e metade
def aumentar(valor=0, taxa=10, formatado=False):
    resp = valor + (valor * taxa / 100)
    return resp if formatado is True else moedando(valor)


def diminuir(valor=0, taxa=10, formatado=False):
    resp = valor - (valor * taxa / 100)
    return resp if formatado is True else moedando(valor)


def dobro(valor=0, formatado=False):
    resp = valor * 2
    return resp if formatado is True else moedando(valor)


def metade(valor=0, formatado=False):
    resp = valor / 2
    return resp if formatado is True else moedando(valor)

def moedando(valor=0, moeda='R$'):
   return f'{moeda}{valor:>8.2f}'.replace('.', ',')

def resumo(valor=0, taxaAumento=10, taxaReducao=5):
    print('-=-'*15)
    print(f'{"RESUMO DO VALOR":^45}')
    print('-=-'*15)
    print(f'Preço analisado: {moedando(valor)}')
    print(f'O dobro do preço: {dobro(valor, False)}')
    print(f'A metade do preço: {metade(valor)}')
    print(f'{taxaAumento}% de aumento: \t{aumentar(valor, taxaAumento, True)}')
    print(f'{taxaReducao}% de redução: \t{diminuir(valor, taxaReducao, True)}')
    print('-=-'*15)
