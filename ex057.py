# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

verif = 0

while verif == 0:
    sexo = str(input('Qual seu sexo?\nDigite M para masculino e F para Feminino:')).upper()
    if sexo == 'M':
        print('Seu sexo é masculino')
        verif = 1
    elif sexo == 'F':
        print('Seu sexo é feminino')
        verif = 1
    else:
        print('Favor não digitar um 3° sexo.')
        verif = 0
