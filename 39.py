'''
Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
'''
import numpy as np
import random
n=int(input('Enter count of elements'))
a=np.zeros((n),dtype=int)
sum=0
for i in range(n):
    a[i]=random.randint(-5,10)
for i in range(n):
    if a[i]%2==0:
        sum+=a[i]
        if a[i]==0:
            break

print(f'Your arr:{a}\nYour sum:{sum}')