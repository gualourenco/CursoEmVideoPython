for c in range(1, 10):
    print(c)

b = 1
while b < 10:
    print(b)
    b += 1
print('Fim')

# n = 1
r = 'S'

# while n != 0:
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

num = 1
par = impar = 0

while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Acabou')
