import numpy as np
import matplotlib.pyplot as plt


n_y=np.linspace(0,9,10)

y=np.loadtxt("ques_3/y__n.dat")

n_x=np.linspace(0,5,6)

plt.subplot(212)
plt.stem(n_y,y)
plt.grid()
# plt.xlabel("n")
plt.ylabel("y(n)")

x=[1,2,3,4,2,1]

plt.subplot(211)
plt.stem(n_x,x)
plt.grid()
plt.ylabel("x(n)")
plt.xlabel("n")


plt.show()