'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
'''
import numpy as np
import random
n=int(input('Enter your count of els:'))
a=np.zeros((n),dtype=int)
mid=0
count=0
for i in range(n):
    a[i]=random.randint(-15,20)
    if -2<=a[i]<=10:
        mid+=a[i]
        count+=1
mid//=count
print(f'Your arr:{a}\nYour count of nums:{count}\nYour middle value:{mid}')