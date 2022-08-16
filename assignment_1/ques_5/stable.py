import numpy as np
import matplotlib.pyplot as plt
from mpmath import nsum, exp, inf,quad




def u(n):
    if n>=0:
        return 1
    else:
        return 0

def h(n):
    return (-1/2)**n*u(n)+(-1/2)**(n-2)*u(n-2)
l=0
for i in range(1000):
    l+=h(i)

print(l)