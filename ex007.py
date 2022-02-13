# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média entre a nota {nota1} e a nota {nota2} é {media}')

notas = [nota1, nota2]
x = 0
for nota in notas:
    x += 1

print(f'A Media de {nota1} e {nota2} é {(nota1+nota2)/x}')
