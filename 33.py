'''
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
'''
import numpy as np
import random
n=20
a=np.zeros((n),dtype=int)
doubt=1
for i in range(n):
    a[i]=random.randint(-10,10)
    if a[i]!=0:
        doubt*=a[i]
print(f'Your arr:{a}\nYour doubt:{doubt}')