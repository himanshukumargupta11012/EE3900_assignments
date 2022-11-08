import numpy as np
import math as mt
import matplotlib.pyplot as plt

def x(t):
    return A*abs(mt.sin(2*np.pi*f*t))

A=12
f=50

x_vec=np.vectorize(x)
k=np.linspace(-10,10,1000)
plt.plot(k,x_vec(k),label="x(t)")
plt.grid()
plt.legend()
plt.ylabel("$x(t)$")
plt.xlabel("$t$")
plt.savefig("./1.1.png")
plt.show()



