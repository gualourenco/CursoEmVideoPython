# Refaça o Desafio 035, dos triânulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: Todos os lados diferentes

reta1 = float(input('Primeira reta:'))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))


if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('Legal! As retas formam um triângulo')
    if reta1 == reta2 == reta3:
        print('As retas formam um triângulo Equilátero')
    elif reta1 != reta2 != reta3 != reta1:
        print('As retas formam um triângulo Escaleno')
    else:
        print('As retas formam um triângulo Isóceles')
else:
    print('As retas não formam triângulo')
