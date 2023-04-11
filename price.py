'''
создали модуль с функцией discounted
для подсчета суммы с заданной скидкой
'''

def discounted(price, discount, max_discount=100): #третий именованный аргумент(со значением по умолчанию)
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    
    if discount >= max_discount:
        price_with_discount = price
        return f'Ваша сумма составляет {price_with_discount}р.'
    else:
        price_with_discount = price - (price * discount / 100)
        return f'Ваша сумма с учетом скидки {price_with_discount}р.'
    
product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 50}

product['with_discount'] = discounted(product['price'], product['discount'])
