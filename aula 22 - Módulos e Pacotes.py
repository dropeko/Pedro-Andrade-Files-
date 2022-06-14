# AULA 22 - MÓDULOS E PACOTES
#MÓDULOS
#Ex: Criando um programa e chamando o módulo onde estão as FUNÇÕES
import FUNCIONALIDADES
numglobal = int(input('Digite um número para calcular o fatorial: '))
fatglobal = FUNCIONALIDADES.fatorial(numglobal)
dobroglobal = FUNCIONALIDADES.dobro(numglobal)
triploglobal = FUNCIONALIDADES.triplo(numglobal)
print(f'O fatorial do número {numglobal} é {fatglobal}')
print(f'O dobro do número {numglobal} é {dobroglobal}')
print(f'O triplo do número {numglobal} é {triploglobal}')
#-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----##-----#
# PACOTES
# Uma pasta que CONTÉM MÓDULOS
# Dentro de cada módulo DENTRO dos pacotes, existe um arquivo: __init__.py
# Criando um pacote e colocando módulos dentro dele
# -> Dentro do projeto -> New -> Python Package
from Funcionalidades import Numeros
numg2 = int(input('Digite um número: '))
fatg = Numeros.fatorial(numg2)
dobrog2 = Numeros.dobro(numg2)
triplog2 = Numeros.triplo(numg2)


