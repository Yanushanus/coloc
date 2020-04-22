'''Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.'''
import numpy as np
import random
n=int(input('Enter your count of els:'))
a=np.zeros((n),dtype=int)
k=int(input('Enter your noun:'))
count=0
t=False
max=0
for i in range(n):
    a[i]=random.randint(-15,20)
    if a[i]>max:
        max=a[i]
for i in range (n):
    if max==a[i]:
        count+=1
if max<k and count==1:
    t=True
print(f'Your arr:{a}\nAnd your t is {t}')