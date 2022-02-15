# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagemno final,
# de acordo com a média atingida
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

n1 = float(input('Insira a primeira nota:'))
n2 = float(input('Insira a segunda nota:'))

media = (n1 + n2) / 2
if media < 5.0:
    print(f'A média é {media:.1f}: Reprovado')
elif 5.0 <= media <= 6.9:
    print(f'A média é {media:.1f}: Recuperação')
else:
    print(f'A média é {media:.1f}: Aprovado')
