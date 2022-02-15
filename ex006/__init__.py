# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = int(input('um numero inteiro: '))

dobro = n*2
triplo = n*3
raiz = n**(1/2)

print(f'O numero escolhido foi: {n}\nSeu dobro é {dobro}\nO triplo {triplo}\nSua raiz é {raiz:.2f}')
