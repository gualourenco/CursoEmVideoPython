# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.

pessoas = []
homemvelho = 0
nomehomem = ''
mulheresnovas = 0
media = 0

while len(pessoas) < 4:
    print(f'--- {len(pessoas)+1} Pessoa ---')
    pessoa = [str(input('Nome: ')), int(input('Idade: ')), str(input('Sexo: '))]
    pessoas.append(pessoa)

for c in pessoas:
    media += c[1]
    if c[1] < 20 and c[2] == 'f':
        mulheresnovas += 1
    elif c[2] == 'm':
        if homemvelho < c[1]:
            nomehomem = c[0]
            homemvelho = c[1]

print(f'A média das pessoas são de {media / len(pessoas)} anos.'
      f'\nO homem mais velho é o {nomehomem}, com {homemvelho}, e temos {mulheresnovas} mulheres com menos de 20 anos')
