print('-=-'*10)
print('   GERENCIADOR DE PAGAMENTOS')
print('-=-'*10)
val = float(input('Qual o valor das compras?: R$'))
print('''FORMAS DE PAGAMENTO:
 [ 1 ] À vista dinheiro/cheque
 [ 2 ] À vista no cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')
op = int(input('Qual será a opção de pagamento?: '))
if op == 1:
    novoval = val - (val * 10/100)
    print('No pagamento à vista com dinheiro/cheque o desconto é de 10%! \n Valor a pagar: R${}'.format(novoval))
elif op == 2:
    novoval = val - (val * 5/100)
    print('Pagamento a vista no cartão tem 5% de desconto! \n Valor a pagar: R${}'.format(novoval))
elif op == 3:
    print('Valor a pagar pela compra: R${}'.format(val))
elif op == 4:
    novoval = val + (val * 20/100)
    print('Dividir no cartão tem acréscimo de 20% de juros! \n Valor a pagar: R${}'.format(novoval))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!!')
