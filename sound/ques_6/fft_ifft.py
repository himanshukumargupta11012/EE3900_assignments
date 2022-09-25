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

def y(n):
    if n<0:
        return 0
    else :
        return -1/2*y(n-1)+x(n)+x(n-2)


k=np.arange(N)
h_vec=np.vectorize(h)
x_vec=np.vectorize(x)
y_vec=np.vectorize(y)
x_k=x_vec(k)
h_k=h_vec(k)
y_k=y_vec(k)

X_k_fft=fft(x_k)
H_k_fft=fft(h_k)

Y_k_fft=[H_k_fft[i]*X_k_fft[i] for i in k]




def dft(k,fn):
    l=0
    for i in range(N):
        l+=fn(i)*np.exp(-1j*2*np.pi*k*i/N)
    return l

dft2=np.vectorize(dft)

X_k=dft2(k,x)
H_k=dft2(k,h)


Y_k=[X_k[int(i)]*H_k[int(i)] for i in k]



def idft(k):
    l=0
    for i in range(N):
        l+=Y_k[i]*np.exp(1j*2*np.pi*k*i/N)
    return l/N

idft_vec=np.vectorize(idft)


y_k_idft=idft_vec(k)



y_k_ifft=ifft(Y_k)

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

plt.stem(k,np.real(y_k_ifft), markerfmt='bo')
plt.stem(k,y_k,linefmt='g-.' ,markerfmt='go')
plt.stem(k,np.real(y_k_idft),linefmt='r:',markerfmt='ro')

plt.xlabel("k")
plt.ylabel("$y(n)$")
plt.xticks(k)
plt.grid ()
plt.legend(["IFFT","DIff. Eqn.","IDFT"])
plt.show()
