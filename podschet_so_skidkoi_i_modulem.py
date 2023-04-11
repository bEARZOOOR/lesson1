
'''
Импортируем модуль price.py и используем
функцию discounted для подсчета
'''

import price2 as p

count = p.discounted
result = count(input('Введите сумму: '), input('Введите сумму скидки: '))
print(result)
