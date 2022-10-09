import numpy as np

x=[2,-1]
b=[-1,2,1]

y=np.convolve(b,x)

print(y)