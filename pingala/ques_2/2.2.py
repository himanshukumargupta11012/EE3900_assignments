import matplotlib.pyplot as plt
import numpy as np

def x(n):
  if n<0:
    return 0
  if n==1 or n==0:
    return 1
  else:
    return x(n-1)+x(n-2)


x_vec=np.vectorize(x)
k=np.arange(10)

plt.stem(k,x_vec(k))
plt.grid()
plt.xlabel("$n$")
plt.ylabel("$x(n)$")
plt.xticks(k)
plt.show()