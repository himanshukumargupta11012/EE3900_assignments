import numpy as np
import matplotlib.pyplot as plt

N=20

def x(n):
    if n<0 or n>5:
        return 0
    elif n<4:
     return n+1
    else:
        return 6-n

def h(n):
    if n<0:
        return 0
    elif n<2:
        return (-1/2)**n
    else:
        return 5*(-1/2)**n
def dft(k,fn):
    l=0
    for i in range(N):
        l+=fn(i)*np.exp(-1j*2*np.pi*k*i/N)
    return l



k=np.linspace(0,N-1,N)
dft2=np.vectorize(dft)

X=dft2(k,x)
H=dft2(k,h)
# print(X)

plt.subplot(211)
plt.stem(k,np.real(X))
plt.grid ()
plt.ylabel("$X(k)$")

plt.subplot(212)
plt.stem(k,np.real(H))
plt.xlabel("k")
plt.ylabel("$H(k)$")
plt.grid ()
plt.show()
