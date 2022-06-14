# AULA 20 - FUNÇÕES 1 - ROTINAS
def lin(): # Função SEM parâmetro
    print('-'*40)

# SEMPRE dar duas linhas de espaço da função para o programa principal
lin()
print(f'{"CURSO EM VÍDEO":^40}')
lin()
lin()
print(f'{"ESTRUTURAS COMPOSTAS":^40}')
lin()
lin()
print(f'{"PYTHON 3":^40}')
lin()
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
def mensagem(msg):# Função COM paramêtro
    print('-'*40)
    print(msg) #Imprimindo o parâmetro
    print('-'*40)

# SEMPRE dar duas linhas de espaço da função para o programa principal
mensagem(f'{"CURSO EM VÍDEO PYTHON - ESTRUTURAS COMPOSTAS":^40}')
mensagem(f'{"OLHA COMO ISSO AQUI TA MUITO BOM":^40}')
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
def soma(a, b):
    s = a + b
    print(s)

#Programa Principal
soma(6, 7)
soma(a=1, b=3)
soma(b=3, a=7)
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
#DEFININDO FUNÇÃO COM DESEMPACOTAMENTO
def soma(*valores):
    s = 0
    for numeros in valores:
        s = s + numeros
    print(f'Somando os {valores} temos {s}')

soma(3, 5)
soma(3, 7, 5, 4)
soma(1, 5, 9, 3)
#---------##---------##---------##---------##---------##---------##---------##---------##---------##---------##---------#
# DEFININDO FUNÇÃO COM LISTA
def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst = lst * 2
        posicao = posicao + 1



valores = [4, 3, 7, 5, 9]
dobra(valores)
print(valores)