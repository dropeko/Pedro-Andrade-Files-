import moeda
print('-=-'*15)
print(f'{"MÓDULOS EM PYTHON":^45}')
print('-=-'*15)
preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moedando(preco, "US$")} é {moeda.metade(preco)}')
print(f'O dobro de {moeda.moedando(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10% no preço, temos {moeda.aumentar(preco)}')
print(f'Diminuindo 10% no preço, temos {moeda.diminuir(preco, True)}')
