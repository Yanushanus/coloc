''' Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього.'''

n=5
a=[]
for i in range (n):
   a.append(input(f'Enter {i+1} surname'))
k=a[::-1]
for i in k :
    print(i)