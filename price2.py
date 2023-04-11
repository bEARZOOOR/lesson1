'''
создали модуль с функцией discounted
для подсчета суммы с заданной скидкой!!!
'''

def discounted(price, discount, max_discount=99): #третий именованный аргумент(со значением по умолчанию)
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    
    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 99%.')
    if discount >= max_discount:
        return f'Без учета скидки {price}'
    else:
        return f'С учетом скидки {price - (price * discount / 100)}'
    
product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 50}

product['with_discount'] = discounted(product['price'], product['discount'])

print(discounted(100, 60))