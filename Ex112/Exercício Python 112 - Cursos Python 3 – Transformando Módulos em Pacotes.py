from Ex112.UtilidadesCeV import Moeda
from Ex112.UtilidadesCeV import Dado
print('-=-'*15)
print(f'{"MÓDULOS EM PYTHON":^45}')
print('-=-'*15)
preco = Dado.leiaDin('Digite o preço: R$')
Moeda.resumo(preco, 20, 15)