# AULA 19 - DICIONÁRIOS - Estrutura de dados com indices literais
# DADOS --> Pedro, 27 anos
dicionario = dict()
dados = {'nome': 'Pedro', 'idade': 27, 'sexo': 'M'}
print(dados)
del dados['idade']
#-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----#

filme = {'Titulo': 'Star Wars',#Criando um dicionário
         'Ano': 1977,
         'Diretor': 'George Lucas'
}
print(filme.values())#Imprime os valores armazenados nas chaves
print(filme.keys())#Imprime as chaves do dicionário
print(filme.items())#Imprime os valores e chaves juntos

#-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----#
for chaves, valor in filme.items():#Varrendo o dicionário para imprimir cada CHAVE com seu respectivo VALOR
    print(f'O {chaves} é {valor}')
#-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----#

#Você PODE juntar LISTAS, TUPLAS E DICIONÁRIOS
locadora = list()
filme1 = {'Titulo': 'Avengers',#Criando um dicionário
         'Ano': 2012,
         'Diretor': 'Marvel'
}
filme2 = {'Titulo': 'Matrix',#Criando um dicionário
         'Ano': 1999,
         'Diretor': 'Wachowski'
}
locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)
print(locadora[1]['Titulo'])#locadora[1]<- referência externa ['Titulo']<- referência interna
print(locadora[2]['Ano'])#locadora[2]<- referência externa ['Ano']<- referência interna
print(locadora[0]['Diretor'])#locadora[0]<- referência externa ['Diretor']<- referência interna
#-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----#

pessoas = {'nome': 'Pedro', 'idade': 27, 'sexo': 'M'}
print(pessoas['nome'])
pessoas['peso'] = 80.7 #Cria um elemento no final e adiciona o valor designado
for chaves in pessoas.keys():
    print(chaves)
for valor in pessoas.values():
    print(valor)
for chaves, valor in pessoas.items():
    print(f'{chaves} = {valor}')
#-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----#

estado = {}
brasil = []
for cont in range(0,3):# Lendo 3 informaçoes ao dicionário e adicionando em uma lista
    estado['UNIDADE FEDERATIVA'] = str(input('Digite o estado: '))
    estado['SIGLA'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())#Copiando o dicionário para dentro da lista
for estadolooping in brasil:
    for valor in estadolooping.values():
        print(valor, end=' -> ')
    print()
