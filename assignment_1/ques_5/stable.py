import numpy as np
import matplotlib.pyplot as plt
from mpmath import nsum, exp, inf,quad




def u(n):
    if n>=0:
        return 1
    else:
        return 0

def h(n):
    (-1/2)**n*u(n)+(-1/2)**(n-2)*u(n-2)
# l=0
# for i in range(-int(np.inf),int(np.inf)):
#     l+=h(i)
sum=quad(lambda x: h(x), [-inf, inf])
print(l)