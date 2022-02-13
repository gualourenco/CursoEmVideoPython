
frase = 'Curso em video python'

# frase[9]
# frase[9:13]
# frase[9:21]
# frase[9:21:2]
# frase[:5]
# frase[15:]
# frase[9::3]

len(frase)
frase.count('o')
frase.count('o', 0, 13)
frase.find('deo')
frase.find('Android')
# 'curso' in frase

# transformacao

frase.replace('Python', 'Adroid')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()
frase_troca = frase.replace('Python', 'Android')
lista_frase = frase.split()
nova_frase = '-'.join(lista_frase)

frase2 = '   Aprenda Python  '
frase2.strip()
frase2.rsplit()
frase2.lstrip()
