'''
Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
'''
import numpy as np
a = np.random.randint(0, 101, 10)
l = []
for i in range(len(a)):
    if a[i] -10 >i:
        l.append(a[i])
a = np.array(l)
print(a)

if len(a) == 0:
    print('No el like you want')

