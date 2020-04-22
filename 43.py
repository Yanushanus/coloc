'''Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.'''
import numpy as np
import random
n=int(input('Enter your count of els:'))
arr=np.zeros((n),dtype=int)
count=0
for i in range(n):
    arr[i]=random.randint(-10,20)
    if arr[i]==i and arr[i]%3==0:
        count+=1
print(f'Your arr:{arr}\nYour count:{count}')