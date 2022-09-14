import re

num = "^(0(,\d{0,2})?|-?[1-9]\d*(,\d{1,20})?|-0,(0[1-9]|[1-9]\d?))$"
id = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

b = '123123,666666'
c = '123c123'

if re.findall(id, b):
    print('sim')