import numpy as np
import matplotlib.pyplot as plt

n_1=np.arange(0, 17)
n_2=np.array([3, 9, 15])
y1=np.loadtxt("series.txt", delimiter=" ", max_rows=1)
y2=y1[n_2]
plt.stem(n_1, y1, markerfmt='.', linefmt='-') 
plt.stem(n_2, y2, markerfmt='o', linefmt='-') 

plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem plot of x(n)')
plt.savefig('../figs/A_1.png')
