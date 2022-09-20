import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft

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

k=np.arange(N)
h_vec=np.vectorize(h)
x_vec=np.vectorize(x)

x_k=x_vec(k)
h_k=h_vec(k)

X_k=fft(x_k)
H_k=fft(h_k)
print(X_k)

Y_k=[H_k[i]*X_k[i] for i in k]


y_k=ifft(Y_k)

plt.subplot(211)
plt.stem(k,np.real(X_k))
plt.grid ()
plt.ylabel("$X(k)$")

plt.subplot(212)
plt.stem(k,np.real(H_k))
plt.xlabel("k")
plt.ylabel("$H(k)$")
plt.grid ()
plt.show()

plt.stem(k,np.real(Y_k))
plt.grid()
plt.xlabel("k")
plt.ylabel("$Y(k)$")
plt.show()

plt.stem(k,np.real(y_k))
plt.xlabel("k")
plt.ylabel("$y(n)$")
plt.xticks(k)
plt.grid ()
plt.show()
