from Ex115C.biblio.interface import *

def arquivoExiste(nomearquivo):
    try:#Usando tratamento de erros para verificar se o arquivo existe
        arq = open(nomearquivo, 'rt')# Se HOUVER o arquivo, abrirá como read text
        arq.close()#Fechando o arquivo
    except FileNotFoundError:#Se retornar com o erro pela falta do arquivo
        return False
    else:#Se encontrar o arquivo
        return True


def criarArquivo(novoarquivo):# Função para criar novo arquivo caso não exista no sistema
    try:
        arq = open(novoarquivo, 'wt+')# wt+ -> write text create
        arq.close()
    except:
        print('HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO')
    else:
        print(f'ARQUIVO {novoarquivo} CRIADO COM SUCESSO')


def lerArquivo(nomearquivo):
    global arq
    try:
        arq = open(nomearquivo, 'rt') #Tentando ler o arquivo e abrindo como read text
    except:
        print('ERRO AO LER O ARQUIVO !')
    else:
        cabecalho('PESSOAS CADASTRADAS')#Se houver o arquivo imprimi as pessoas cadastradas com o texto formatado
        for linha in arq:#Estrutura de repetição for para imprimir nome e idade por linha
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arq.close()



def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} cadastrado com SUCESSO!')

