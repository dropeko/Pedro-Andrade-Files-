#AULA 21 - FUNÇÕES 2
# INTERACTIVE HELP #
help() # <- Função interna do Py
help(print)
print(input.__doc__) # Função para imprimir o comando INPUT
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
# DOCSTRINGS #
def contador(i, f, p):# Docstring é feito por aspas triplas logo abaixo do comando DEF
    """
    -> Faz uma contagem e mostra na tela
    :para i: inicio da contagem
    :para f: fim da contagem
    :para p: passo da contagem
    :return: sem retorno
    """
    cont = i
    while cont <= f:
        print(f'{cont}... ', end='')
        cont = cont + p
    print('FIM!')


contador(0, 100, 10)
help(contador)
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
# FUNÇÕES COM PARAMÊTROS OPCIONAIS #
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma de todos os valores é: {s}')
    print()
soma(7, 2, 5)
soma(7, 4)
soma(7)
soma()
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
# ESCOPO DE DECLARAÇÕES DE VARIAVEIS - LOCAL ONDE A VARIAVEL VAI OU NÃO EXISTIR
# Escopo GLOBAL e Escopo LOCAL
def teste(b):
    global a
    b = b + 4
    c = 2
    a = 8
    print(f'B dentro vale {b}')#9
    print(f'C dentro vale {c}')#2
    print(f'A dentro vale {a}')#8

#Programa Principal
a = 5
teste(a)
print(f'A fora vale: {a}')#5 e depois de chamar a função receberá o valor 8
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
# FUNÇÕES QUE RETORNAM RESULTADOS #
# Muito uteis quando queremos ter personalização dos resultados
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s #Depois de somar, joga o valor obtido dentro da variavel desginada. Ex: r1, r2, r3

r1 = somar(5, 7, 3)
r2 = somar(7, 7)
r3 = somar(7)
print(f'Meus cálculos deram: {r1}, {r2}, {r3}')
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
def fatorial(num=1): #FUNÇÃO PARA CALCULAR O FATORIAL DE UM NÚMERO
    fat = 1
    for cont in range(num, 0, -1):
        fat = fat * cont
    return fat


f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2}, {f3}')
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#]
def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!!')
else:
    print('Não é par!!')



