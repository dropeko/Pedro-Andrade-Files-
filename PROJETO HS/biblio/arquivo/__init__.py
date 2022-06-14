import biblio.interface
from biblio.interface import *

#Primeiro vamos verificar se o arquivo txt existe
def arquivoExiste(arquivo):
    try:
        arq = open(arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

#Se não houver arquivo, essa função será chamada e criará um arquivo txt com o parametro passado no prog principal
def criarArquivo(novoarquivo):
    try:
        arq = open(novoarquivo, 'wt+')#SEMPRE tentar abrir o arquivo para realiar qualquer ação / 'wt+' -> Cria um arquivo em write text
        arq.close()#Fecha o arquivo para testar se a ação deu certo
    except:#Se o arquivo NÃO for criado
        print(f'HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO {novoarquivo}!!')
    else:#Se o arquivo FOR criado
        print(f'ARQUIVO {novoarquivo} CRIADO COM SUCESSO!!')


def lerArquivo(arquivo):#Função para ler o arquivo
    global arq #Chama o arquivo de escopo GLOBAL
    try:
        arq = open(arquivo, 'rt')#SEMPRE tentar abrir o arquivo para qualquer ação / 'rt' -> abre em read text
    except:#Se houver um ERRO ao ler o arquivo
        print('HOUVE UM ERRO AO LER O ARQUIVO!!')
    else:#Se estiver tudo certo, abre o arquivo em print formatado pelo laço de repetição FOR
        cabeçalho('ANIMAIS CADASTRADOS')#Chama a função de interface CABEÇALHO
        for linha in arq:
            dadolinha = linha.split(';')#Separando os dados cadastrados na string ;
            dadolinha[3] = dadolinha[3].replace('\n', '')
            print(f'\033[32mAnimal:\033[m {dadolinha[0]:<16} \033[32mIdade:\033[m {dadolinha[1]} meses \n\033[32mPai:\033[m {dadolinha[2]} \n\033[32mMãe:\033[m {dadolinha[3]}')
            print(biblio.interface.linha())
    finally:
        arq.close()


def cadastrar(arquivo, nome='SEM NOME', meses=0, pai='SEM NOME', mae='SEM NOME'):
    try:#SEMPRE tentar abrir o arquivo para realizar qualquer operação
        arq = open(arquivo, 'at')
    except:#Se houver problema na leitura do arquivo
       print('HOUVE UM ERRO NA HORA DE CADASTRAR O ANIMAL!')

    else:#Aqui executa a ação de cadastro
        try:
            arq.write(f'{nome};{meses};{pai};{mae}\n') #Realiza o cadastro do animal em linha separado por uma string ; e quebra a linha com \n
        except:
            print('HOUVE UM ERRO NO CADASTRO!')
        else:
            print(f'Cadastro do animal {nome} realizado com SUCESSO! ')
