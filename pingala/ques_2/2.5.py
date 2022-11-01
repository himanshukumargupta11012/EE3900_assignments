import matplotlib.pyplot as plt
import numpy as np

al=(1+np.sqrt(5))/2
be=(1-np.sqrt(5))/2
def x(n):
    if n>0:
        return (al**n-be**n)/(al-be)
    else:
        return 0

def y(n):
    if n>=1:
        return x(n-1)+x(n+1)
    else:
        return 0

k=np.arange(-2,11)
y_vec=np.vectorize(y)
plt.stem(k,y_vec(k))
plt.grid()
plt.savefig("./2.5.png")
plt.show()
