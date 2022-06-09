from biblio.arquivo import *
import time
#Programa Principal
print('-=-'*15)
print(f'{"SISTEMA DE PESSOAS FINAL":^45}')
print('-=-'*15)

arquivo = 'cursoemvideo.txt'
if not arquivoExiste(arquivo):#Verificando por módulos se o arquivo existe
    criarArquivo(arquivo)


while True:# Criando um loop infinito para interação do usuario com o sistema
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resp == 1:
        #Opção de listar o conteudo do arquivo
        lerArquivo(arquivo)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)

    elif resp == 3:#Flag para quebrar o looping e encerrar o sistema
        cabecalho('Saindo do programa... Até logo!')
        time.sleep(0.5)
        break
    else:#Tratamento de erro de digitação pelo usuario
        print(f'\033[0;31mOpção Inválida!! Digite somente uma das {resp} opções!\033[m ')
        time.sleep(1)