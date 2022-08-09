import matplotlib.pyplot as plt
import numpy as np


X=np.array([1,2,3,4,2,1])

Y=np.zeros(20)

Y[0]=X[0]
Y[1]=-1/2*Y[0]+X[1]

for i in range(20):
    if 1<i<6:
        Y[i]=-1/2*Y[i-1]+X[i]+X[i-2]
    if 6<=i<8:
        Y[i]=-1/2*Y[i-1]+X[i-2]
    if 8<=i<20:
        Y[i]=-1/2*Y[i-1]
print(Y)
plt.stem(range(6),X)

plt.grid()
plt.ylabel("x(n)")
plt.xlabel("n")
plt.show()

plt.stem(range(-5,20),np.concatenate((np.zeros(5),Y)))
plt.grid()
plt.ylabel("y(n)")
plt.xlabel("n")
plt.show()