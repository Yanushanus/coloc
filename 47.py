'''
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
'''
import numpy as np
import random
n=10
N=int(input('Enter your num:'))
a=np.zeros(n,dtype=int)
for i in range(n):
    a[i]=random.randint(1,100)
print(f'Lucky tickets:{a}')
if N in a:
    print('Good job,you are lucky')
else:
    print('Try next time')