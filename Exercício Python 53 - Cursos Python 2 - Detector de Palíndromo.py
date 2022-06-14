print('-=-'*10)
print('     DETECTOR DE PALÍNDROMO')
print('-=-'*10)
# Lendo a frase, splitando e jogando tudo pra maiuscula
frase = str(input('Digite uma frase: ').strip().upper())
# Splitando a frase para gerar uma lista
palavras = frase.split()
# Juntando a frase em uma string só
junto = ''.join(palavras)
inverso = ''
# Estrutura for a fim de inverter a frase
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Parabéns!! Temos um PALÍNDROMO!')
else:
    print('Isto NÃO é um PALÍNDROMO!')
