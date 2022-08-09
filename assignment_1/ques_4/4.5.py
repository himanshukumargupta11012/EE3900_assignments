from cmath import cos
import matplotlib.pyplot as plt 
import numpy as np

# direct by code
def H(x):
    return (1+x**(-2))/(1+1/2*x**(-1))
omega=np.linspace(-3*np.pi,3*np.pi,100)
E=[np.exp(1j*x) for x in omega]
H2=np.vectorize(H)

# after solving manually
def mod_H(w):
    return 4*abs(np.cos(w))/np.sqrt(5+4*np.cos(w))
mod_H2=np.vectorize(mod_H)


plt.plot(omega,abs(H2(E)),linewidth=4,color="gold")
plt.plot(omega,mod_H2(omega),linestyle="dashed")

plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})|$')
plt.grid()
plt.show()


# def mod_H(w):
#     return 4*abs(np.cos(w))/(5+4*np.cos(w))
# mod_H2=np.vectorize(mod_H)

# plt.plot(omega,mod_H2(omega))
# plt.show()