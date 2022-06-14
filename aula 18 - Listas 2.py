# AULA 18 - LISTAS 2
galera = [['Pedro', 25], ['Maria', 19], ['João', 32]] #Criando uma lista dentro de OUTRA lista
print(galera[0][0]) #Imprimindo na dela orientando pelos indices / primeiro [] indice de fora / segundo [] indice de dentro
print(galera[1][1]) #Imprimindo na dela orientando pelos indices / primeiro [] indice de fora / segundo [] indice de dentro
print(galera[2][0]) #Imprimindo na dela orientando pelos indices / primeiro [] indice de fora / segundo [] indice de dentro
print(galera[1]) #Imprimindo na tela conjunto 1
for pessoas in galera: # Para cada pessoa em galera, imprima pessoa somente
    print(f'{pessoas[0]} tem {pessoas[1]} anos de idade!')
#--------##--------##--------##--------##--------##--------##--------##--------##--------##--------##--------##--------##--------#
turma = list() #Criando uma lista vazia
pessoa = list() #Criando uma lista vazia
for cont in range(0, 3): # Criando um laço para armazenar dados de 3 pessoas
    pessoa.append(str(input('Digite o nome: '))) #Adicionando nome a lista pessoa
    pessoa.append(int(input('Digite a idade: '))) #Adicionando idade a lista pesso
    turma.append(pessoa[:]) #Criando uma cópia dos dados inseridos em outra lista <------------
    pessoa.clear() #Limpando os dados recebidos para armazenar os novos
print(turma) #Imprimindo o resultado na tela
for pessoas1 in galera: #Para cada pessoa na lista Galera
    if pessoas1[1] >= 21: #Se a idade for maior de 21
        print(f'{pessoas[0]} é maior de idade!!')
    else: #Se a idade for menor de 21
        print(f'{pessoas1[0]} é menor de idade!!')
