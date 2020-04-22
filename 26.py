''' Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у
масив T.'''
import numpy as np
min=42
max=0
middle=0
n=6
T=np.zeros((n),dtype=float)
for i in range(n):
    T[i]=float(input(f'Enter your {i+1} time:'))
    middle+=T[i]
    if T[i]<min:
        min=T[i]
    if T[i]>max:
        max=T[i]
middle/=6
print(f'Your middle temp:{middle}\nYour min temp:{min}\nYour max temp:{max}')
