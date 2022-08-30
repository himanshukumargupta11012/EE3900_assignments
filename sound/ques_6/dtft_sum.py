import numpy as np
import matplotlib.pyplot as plt

N=6

x=[1,2,3,4,2,1]



def X(k):
    l=0
    for i in range(6):
        l+=x[i]*np.exp(-1j*2*np.pi*k*i/N)
    return l
k=np.linspace(0,N-1,N)
X2=np.vectorize(X)

print(X2(k))


plt.subplot(211)
plt.stem(k,np.real(X2(k)))
plt.grid ()
plt.xlabel("k")
plt.ylabel("$X(k)$")

plt.stem(212)
plt.stem(k,np.imag(X2(k)))
plt.xlabel("k")
plt.ylabel("$X(k)$")
plt.grid ()
plt.show()
