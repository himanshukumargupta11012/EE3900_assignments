import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import symbols

#n=symbols("n")
al=(1+math.sqrt(5))/2
be=(1-math.sqrt(5))/2

def a(n):
  return (al**n-be**n)/(al-be)

def LHS1(n):
    sum=0
    for i in range(1,n+1):
        sum+=a(i)
    return sum
def RHS1(n):
    return a(n+2)-1
k=np.arange(1,11)
RHS1_vec=np.vectorize(RHS1)
LHS1_vec=np.vectorize(LHS1)

plt.stem(k,RHS1_vec(k),c='r')
plt.stem(k,LHS1_vec(k),c='g')
plt.grid()
plt.show()


def LHS(k):
    int l=0
    for i in range(1,):
        sum+=
