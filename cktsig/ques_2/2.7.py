import numpy as np
import matplotlib.pyplot as plt

def v(t):
    if t>=0:
        return 4*(1-np.exp(-3*t/2))/3
    else:
        return 0

k=np.linspace(0,5,100)
v_vec=np.vectorize(v)

plt.plot(k,v_vec(k))
plt.axhline(y=4/3,c='r')
plt.legend([r'$\frac{4}{3}(1-e^{-\frac{3}{2}t})u(t)$',r"$\frac{4}{3}$"])
plt.grid()
plt.savefig("./v_t_1.png")
plt.show()
