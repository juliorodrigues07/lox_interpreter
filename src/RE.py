import re

numeros = "^(0(,\d{0,2})?|-?[1-9]\d*(,\d{1,20})?|-0.(0[1-9]|[1-9]\d?))$"
indentificadores = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

b = '123123,666666'
c = '1asda'

if re.findall(numeros, b):
    print('numeros')
elif re.findall(indentificadores, b):
    print('identificadores')