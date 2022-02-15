from datetime import date
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('Digite um ano de nascimento: '))
idade = date.today().year - ano
print(f'Dá {idade} anos')

if idade < 18:
    print(f'Você escapou.\nAinda faltam {18 - idade} anos para se alistar no exercito.')
elif idade > 18:
    print(f'Você esta {idade - 18} anos atrasado. É bom ver isso')
else:
    print(f'Que alegria!!!\nVocê está em tempo de se alistar')
