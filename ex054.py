import datetime

# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior = 0
menor = 0
listagem = 1
lista = []
listamaior = []
listamenor = []
while listagem <= 7:
    ano = int(input(f'Insiria o {listagem}° ano: '))
    lista.append(ano)
    listagem += 1

for c in lista:
    maioridade = datetime.date.today().year - c
    if maioridade >= 18:
        maior += 1
        listamaior.append(c)
    else:
        menor += 1
        listamenor.append(c)

print(f'os anos {listamaior} dão o total de {maior} maiores de idade\n{listamenor} dão o total de {menor}'
      f' menores de idade')
