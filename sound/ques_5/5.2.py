import matplotlib.pyplot as plt
import numpy as np
from sympy import N

n=np.linspace(-2,10,13)
print(n)
def u(x):
    if x<0:
        return 0
    if x>=0:
        return 1

def h(n):
    return (-2)**(-n)*u(n)+(-2)**(-n+2)*u(n-2)

print(h(2))
h2=np.vectorize(h)
print(h2(n))
plt.stem(n,h2(n))
plt.grid()
plt.xlabel("n")
plt.ylabel("h(n)")
plt.show()