import numpy as np
import matplotlib.pyplot as plt

R1=1
R2=2
C=1e-6

def H(s):
    return (1/R2)*1/(1/R1+1/R2+s*C)

H_vec=np.vectorize(H)
k=np.linspace(-5e6,1e6,100)

plt.plot(k,H_vec(k))
plt.grid()
plt.xlabel("s")
plt.ylabel("$H(s)$")
plt.savefig("./4.3.png")
plt.show()
