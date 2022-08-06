import numpy as np
import matplotlib.pyplot as plt



def delta(n):
    if n==0:
        return 1
    else:
        return 0
        
len=10
h=np.zeros(len)
h[0]=1

for i in range(1,len):
    h[i]=-h[i-1]/2+delta(i)+delta(i-2)

x=[1,2,3,4,2,1]
print(len(x))
tople=np.zeros([len(h)+len(x)-1,len(x)])
print(tople)
n=np.linspace(0,len,len)


# y=np.convolve(h[0:10],x)
# print(y)



