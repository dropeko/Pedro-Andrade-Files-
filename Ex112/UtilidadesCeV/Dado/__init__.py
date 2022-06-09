def leiaDin(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO!!!! \"{entrada}\" é um preço inválido!!\033[m')
        else:
            valido = True
            return float(entrada)