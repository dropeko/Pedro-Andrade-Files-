#Aqui irão ficar as funções de interface do programa
def leiaInt(numerodigitado):#Função para verificar se o valor digitado tem erro de VALOR, TIPO ou NÃO foi digitado nenhum valor
    while True:
        try:#Analisando o valor digitado
            num = int(input(numerodigitado))
        except(ValueError, TypeError):#Se houver erro de VALOR ou TIPO aparece esta mensagem
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue #Continua o programa
        except(KeyboardInterrupt):#Se o usuario não digitar nenhum valor e acionar o enter
            print('\033[0;34mO usuário preferiu não digitar nenhum valor')
            return 3 #Retorna valor 3 e ENCERRA O PROGRAMA
        else:
            return num


def linha(tamanho = 40):#Função para imprimir uma linha
    lin = '-' * tamanho
    return lin


def cabeçalho(mensagem):#Função para montar um cabeçalho
    print(linha())
    print(mensagem.center(42))
    print(linha())


def menu(opcoes):#Formatando e imprimindo o menu de opções do programa
    cabeçalho('HARAS SANTANA BH')#Usando a função cabeçalho dentro de outra função
    cont = 1
    for item in opcoes:#Usando laço de repetição FOR para imprimir as opções do programa
        print(f'\033[31m{cont}\033[m - \033[32m{item}\033[m')
        cont = cont + 1
    print(linha())
    opcao = leiaInt('Digite sua opção: ')#Usando a função leiaInt para receber a opção digitada pelo usário
    return opcao


