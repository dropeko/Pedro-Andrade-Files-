#Arquivo armanzenando as funções que serão utilizadas nos exercicios 107 a 112
#Funções aumentar, diminuir, dobro e metade
def aumentar(valor=0, taxa=10, formatado=False):
    resp = valor + (valor * taxa / 100)
    return resp if formatado is False else moedando(valor)


def diminuir(valor=0, taxa=10, formatado=False):
    resp = valor - (valor * taxa / 100)
    return resp if formatado is False else moedando(valor)


def dobro(valor=0, formatado=False):
    resp = valor * 2
    return resp if formatado is False else moedando(valor)


def metade(valor=0, formatado=False):
    resp = valor / 2
    return resp if formatado is False else moedando(valor)

def moedando(valor=0, moeda='R$'):
   return f'{moeda}{valor:>8.2f}'.replace('.', ',')