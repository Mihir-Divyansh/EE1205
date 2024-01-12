import numpy as np
import matplotlib.pyplot as plt

def x(n) :
    return (2**n)/256 if n >=0 else 0

n_1=range(0, 17)
n_2=[4, 10, 16]
y1=[x(n) for n in n_1]
y2=[x(n) for n in n_2]
plt.stem(n_1, y1, markerfmt='.', linefmt='-') 
plt.stem(n_2, y2, markerfmt='o', linefmt='-') 

plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem plot of x(n)')
plt.savefig('A_1.png')

