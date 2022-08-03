import matplotlib.pyplot as plt 
import numpy as np
def H(x):
    return (1+x**(-2))/(1+1/2*x**(-1))

omega=np.linspace(-3*np.pi,3*np.pi,100)

E=[np.exp(1j*x) for x in omega]

H2=np.vectorize(H)

plt.plot(omega,abs(H2(E)))
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})|$')
plt.grid()
plt.show()