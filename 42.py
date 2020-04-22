'''
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
'''
import numpy as np
import random
n=int(input('Enter your count of els:'))
arr=np.zeros((n),dtype=int)
a,b=int(input('Enter your a:')),int (input('Enter your b:'))
w=False
count=0
for i in range(n):
    arr[i]=random.randint(-10,20)
    if arr[i]%a==0 and arr[i]%b!=0:
        count+=1
if count>0:
    w=True
print(f'Your arr:{arr}\nYour w:{w}')
