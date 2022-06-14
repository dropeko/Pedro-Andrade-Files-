print('-=-'*20)
print('           CALCULANDO O IMC')
print('-=-'*20)
alt = float(input('Digite a sua altura (M): '))
peso = float(input('Digite o seu peso atual (KG): '))
imc = peso / (alt ** 2)
print('O seu IMC atual é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no PESO IDEAL!')
elif imc > 25 and imc <= 30:
    print('Você está em SOBREPESO!')
elif imc < 30 and imc <= 40:
    print('Você está OBESO!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')



