import numpy as np
import matplotlib.pyplot as plt

def v(t):
    if t<0:
        return 0
    else:
        return 2*(1+np.exp(-3*t/2*1e6))/3

k=np.linspace(0,1e-5,100)
v_vec=np.vectorize(v)

plt.plot(k,v_vec(k))
plt.axhline(y=2/3,c='r')
plt.legend([r'$\frac{2}{3}(1+e^{-\frac{3}{2C_0}t})u(t)$',r"$\frac{4}{3}$"])
plt.grid()
plt.xlabel('t')
plt.ylabel('$v_{C_0}(t)$')
plt.savefig("./3.4.png")
plt.show()
