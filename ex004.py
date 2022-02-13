# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele

n = input('Digite algo: ')
print('O tipo primitivo é: ', type(n))
print('Só tem espaço?', n.isspace())
print('é numero: ', n.isnumeric())
print('é alfanumerico: ', n.isalnum())
print('é alfabetico: ', n.isalpha())
print('é alfabetico: ', n.isalpha())
print('é alfabetico: ', n.isalpha())
print('A primeira letra é maiuscula? ', n.isupper())
print('são todas minúsculas? ', n.islower())
print('Está capitalizada? ', n.istitle())
