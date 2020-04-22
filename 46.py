'''
У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
'''
import numpy as np
import random
n=10
arr=[np.random.randint(0, 20) for x in range(10)]
max = 0
c = 0
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        c = i
print(f'Your arr:{arr}\nLargest element - {max} on position:{c}')
arr.insert(c + 1, c)
print(f'Your new arr:{arr}')