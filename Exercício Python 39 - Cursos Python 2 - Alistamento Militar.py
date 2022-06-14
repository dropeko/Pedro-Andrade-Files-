import datetime
print('-=-'*20)
print('                    ALISTAMENTO MILITAR')
print('-=-'*20)
anonasc = int(input('Digite o ano de seu nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual - anonasc
if idade < 18:
    falta = 18 - idade
    ano = anoatual + falta
    print('Você ainda não pode se alistar no Exército Brasileiro! \n Ainda falta {} anos \n O ano de alistamento será {}'.format(falta, ano))
elif idade == 18:
    print('Você DEVE se alistar no Exército Brasileiro IMEDIATAMENTE!')
else:
    passou = idade - 18
    ano = anoatual - passou
    print('Você já deveria ter se alistado há {} anos \n O ano de alistamento foi: {}'.format(passou, ano))
