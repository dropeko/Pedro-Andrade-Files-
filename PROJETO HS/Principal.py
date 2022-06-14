from biblio.interface import *
from biblio.arquivo import *
import time
print('-=-'*13)
print(f'{"LISTA DE ANIMAIS HS":^40}')
print('-=-'*13)

arquivo = 'harassantabh.txt' #Definindo o nome do arquivo da base de dados dos animais
if not arquivoExiste(arquivo):#Verificando se o arquivo da BD existe
    criarArquivo(arquivo)#Se não existir, cai nessa condição, chama a função e cria o arquivo
    time.sleep(1)#Aguarda um segundo para funcionamento sistemico

while True:#Estrutura de loop infinito que vai rodar o aplicativo
    resp = menu(['Ver animais cadastrados', 'Cadastrar novo animal', 'Sair do Sistema'])#Armazena na variavel a opçao digitada pelo usuário
    if resp == 1:#Opção para listar o conteúdo do arquivo
        lerArquivo(arquivo)
    elif resp == 2:#Opção de cadastrar novo animal
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome do animal: '))
        meses = int(input('Meses de vida: '))
        pai = str(input('Nome do Pai: '))
        mae = str(input('Nome da Mãe: '))
        cadastrar(arquivo, nome, meses, pai, mae)
    elif resp == 3:#Opção para encerrar programa
        cabeçalho('Saindo do programa... Até logo!')
        time.sleep(1)
        break
    else:#Tratamento de erro para que seja digitada somente as opções disponiveis
        print(f'\033[31mERRO!!\033[m Digite apenas uma das 3 opções! ')