import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

numero1 = input('digite um número: ')
numero2 = input('digite outro número: ')

print()

if is_number(numero1) and is_number(numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)
else:
    print('inválido')

# outra solução

print()

numero3 = input('digite um número: ')
numero4 = input('digite outro número: ')

try:
    numero3 = float(numero3)
    numero4 = float(numero4)

    print(numero3 + numero4)
except:
    print('inválido')
