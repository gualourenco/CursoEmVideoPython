# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metro = float(input())
dam = metro / 10
hm = dam / 10
km = hm / 10
dm = metro * 10
cent = dm * 10
mili = cent * 10
print(f'Com {metro}m, temos:\nKilometros: {km}km\nHectometros: {hm}hm\nDecametros: {dam}\nDecimetros: {dm}dm'
      f'\nCentimetros: {cent}cm\nMilimetros: {mili}mm')
