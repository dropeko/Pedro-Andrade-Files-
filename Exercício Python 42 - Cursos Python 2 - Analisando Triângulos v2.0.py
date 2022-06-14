print('-=-'*20)
print('                 ANALISANDO UM TRIÂNGULO')
print('-=-'*20)
lado1 = int(input('Digite o comprimento do 1o lado: '))
lado2 = int(input('Digite o comprimento do 2o lado: '))
lado3 = int(input('Digite o comprimento do 3o lado: '))
# Analisando os lados a fim de veriricar se pode formar um triângulo
if lado1 < lado2 + lado3 and lado2 < lado1 +lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM formar um triângulo!')
# Analisando os lados a fim de verificar QUAL triângulo pode ser formado
    if lado1 == lado2 and lado2 == lado3:
        print('O triângulo formado acima é EQUILÁTERO!')
    elif lado1 == lado2 or lado1 == lado3:
        print('O triângulo formado acima é ISÓSCELES!')
    else:
        print('O triângulo formado acima é ESCALENO')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')

