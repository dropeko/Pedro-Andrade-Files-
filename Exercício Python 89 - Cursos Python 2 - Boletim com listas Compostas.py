print('-=-'*10)
print('   BOLETIM COM LISTAS COMPOSTAS')
print('-=-'*10)
ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1a nota: '))
    nota2 = float(input('Digite a 2a nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-'*10)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=-'*10)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('='*40)
while True:
    perg = int(input('Quer ver a nota de qual aluno? (999 interrompe): '))
    if perg == 999:
        break
    if perg <= len(ficha) - 1:
        print(f'Notas do aluno {ficha[perg][0]}: {ficha[perg][1]}')
print('-=-'*10)
print(f'{"FIM":^20}')