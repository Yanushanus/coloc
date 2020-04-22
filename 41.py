'''
Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
'''
import numpy as np
import random
import math
n=int(input('Enter your count of els:'))
a=np.zeros((n),dtype=int)
count=0
for i in range(n):
    a[i]=random.randint(0,20)
    if i*i<a[i]<math.factorial(i):
        count+=1
print(f'Your arr:{a}\nYour count:{count}')