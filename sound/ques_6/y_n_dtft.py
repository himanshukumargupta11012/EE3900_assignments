from dtft_sum import X,H,k,N
import matplotlib.pyplot as plt
import numpy as np

# print(k)
Y=[X[int(i)]*H[int(i)] for i in k]

print(Y)

plt.stem(k,np.abs(Y))
plt.grid()
plt.xlabel("k")
plt.ylabel("$Y(k)$")
plt.show()

def idft(k):
    l=0
    for i in range(N):
        l+=Y[i]*np.exp(1j*2*np.pi*k*i/N)
    return l/N

idft2=np.vectorize(idft)

plt.stem(k,np.real(idft2(k)))
plt.xlabel("k")
plt.ylabel("$y(n)$")
plt.xticks(k)
plt.grid ()
plt.show()
