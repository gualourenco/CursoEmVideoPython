# \033[0;33;44m - Style; text; back
# Style: 0 = none 1 = bold 4 = underline 7 = negative
#     Style                         Text---Color---Back
#       0 = none                     30 =  branco = 40
#       1 = bold                     31 = vermelho= 41
#       4 = underline                32 =  verde  = 42
#       7 = negative                 33 = amarelo = 43
#                                    34 =  azul   = 44
#                                    35 =  roxo   = 45
#                                    36 =  ciano  = 46
#                                    37 =  cinza  = 47

print('\033[0;;41mOlá Mundo!\033[m')
print('\033[4;33;44mOlá Mundo!\033[m')
print('\033[0;35;43mOlá Mundo!\033[m')
print('\033[0;;42mOlá Mundo!\033[m')
print('\033[7;;40mOlá Mundo!\033[m')
print('\033[0;30;47mOlá Mundo!\033[m')
