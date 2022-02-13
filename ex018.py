# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians

a = float(input())
sen = sin(radians(a))
coss = cos(radians(a))
tan = tan(radians(a))

print(f'Do angulo {a} temos:\nSeno: {sen:.2f}\nCosseno: {coss:.2f}\nTangente: {tan:2f}')
