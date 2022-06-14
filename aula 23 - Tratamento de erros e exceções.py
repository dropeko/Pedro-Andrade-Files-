# AULA 23 - TRATAMENTO DE EXCEÇÕES
try:#AQUI VAI A OPERAÇÃO
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except:#Se tentar a estruta de cima e falhar, o que vai acontecer
    print('Infelizmente tivemos um problema!')
else:# Se a estrutura TRY funcionou / Cláusula OPICIONAL
    print(f'O resultado da divisão é: {r}')
finally:#Acontece independente se deu certo ou erro
    print('Volte Sempre, Muito Obrigado!')
