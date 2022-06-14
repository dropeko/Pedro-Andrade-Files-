# AULA 17 - LISTAS 1
lanche = ['Suco', 'Açai', 'Sanduiche', 'Sorvete']
lanche[2] = 'Crepe' # Substituindo o valor da lista. Sanduiche -> Crepe
lanche.append('Cookie') # Adicionando um novo elemento a lista. Adiciona no final da lista
lanche.insert(0, 'Hot Dog') # Adiciona um novo elemento a lista. É possivel definir a posição / .insert(posição, valor)
del lanche[1] # Deleta o elemento pelo indice
lanche.pop() # Normalmente usado para eliminar o ultimo valor da lista
lanche.remove('Sorvete') # Elimina o elemento pelo valor, não pelo indice. Elimina só a PRIMEIRA ocorrência
if 'Suco' in lanche: # Estrutura a fim de verificar se o valor está na lista e elimina-lo
    lanche.remove('Suco')
else:
    print('Não achei o número na lista')

lista = list(range(0, 10)) # Criando uma lista com a função LIST e de range 0 a 10
lista.sort() # Enumera a lista em ordem crescente
lista.sort(reverse=True) # Organiza a lista em ordem DECRESCENTE
len(lista) # Usado para fazer laços com listas e saber a quantidade de elementos

# Solicitando valores para adicionar a lista
valores = list() # Iniciando a lista vazia
for cont in range(0, 6): # Definindo 6 elementos para adicionar a lista
    valores.append(int(input(f'Digite o {cont+1}º valor: ')))
for indice, valor in enumerate(valores): # Imprimindo a lista com o a posição e o valor
    print(f'Encontrei na {indice + 1}ª posição o valor: {valor}!')
print('CHEGUEI AO FINAL DA LISTA! :B')

# Criar cópia ou ligação entre listas
a = [2, 4, 5, 7]
b = a #Cria uma LIGAÇÃO entre as listas... se alterar b ALTERA a
b2 = a[:] # Cria uma CÓPIA da lista... se alterar b NÃO ALTERA a
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista B2: {b2}')
