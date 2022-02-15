from datetime import date
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
# - Até 9 Anos: Mirim
# - Até 14 Anos: Infantil
# - Até 19 Anos: Junior
# - Até 25 Anos: Sênior
# - Acima: Master

ano = int(input('Digite o ano de nascimento do atleta:'))
idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos: Mirim')
elif idade <= 14:
    print(f'O atleta tem {idade} anos: Infantil')
elif idade <= 19:
    print(f'O atleta tem {idade} anos: Junior')
elif idade <= 25:
    print(f'O atleta tem {idade} anos: Sênior')
else:
    print(f'O atleta tem {idade} anos: Master')
