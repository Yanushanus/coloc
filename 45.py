'''Задана таблиця назв товарів, що випускаються заводом. Визначте, чи
повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть
назву першого товару з таблиці.'''
goods = ['knife', 'fork', 'plate', 'table', 'chair', 'knife']
print('Goods list:')
for name in goods:
    print('‣', name)
if goods.count(goods[0]) > 1:
    duplicate = goods[0]
    while duplicate in goods:
        goods.remove(duplicate)
print('New list:')
for name in goods:
    print('‣', name)