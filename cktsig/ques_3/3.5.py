import numpy as np
import matplotlib.pyplot as plt


data=np.loadtxt('./3.5.dat',dtype='double')

time=data[:,0]
v_anal=data[:,1]

def v_theo(t):
    if t>=0:
        return 2*(1+np.exp(-3*t/2*1e6))/3
    else:
        return 0

v_theo_vec=np.vectorize(v_theo)
plt.plot(time,v_theo_vec(time),label='theoretical')
plt.plot(time,v_anal,'o',label='analytical')
plt.legend()
plt.grid()
plt.savefig('./3.5.png')
plt.show()


