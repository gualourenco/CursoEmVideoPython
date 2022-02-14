from datetime import date
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano: Obs:Coloque 0 para analizar o ano atual'))
# um ano divisivel por 4, é bissexto
# um ano divisivel por 100 e por 400, é bissexto
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        print(f'O ano {ano} é Bissexto')
    else:
        print(f'O ano {ano} não é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')

# ou

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')
