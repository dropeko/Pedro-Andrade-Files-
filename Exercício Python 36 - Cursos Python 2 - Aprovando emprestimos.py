print ('-=-'*20)
print('          ANALISANDO EMPRÉSTIMOS')
print('-=-'*20)
# Recebendo os valores para armazenar nas variaveis
casa = float(input('Qual o valor da casa que quer comprar?: R$'))
sal = float(input('Qual é o seu salário atual?: R$'))
fin = float(input('Em quantos anos pretende financiar a casa?: '))
# Realizando o calculo do valor da prestação
prest = casa / (fin * 12)
# Adicionando a estrutura condicional
if prest > (sal * 30/100):
    print('Empréstimo NEGADO')
else:
    print('Empréstimo CONCEDIDO')
