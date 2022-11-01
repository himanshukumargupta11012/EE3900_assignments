import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import symbols

#n=symbols("n")
al=(1+math.sqrt(5))/2
be=(1-math.sqrt(5))/2

def a(n):
    if n>=1:
        return (al**n-be**n)/(al-be)
    else:
        return 0

def b(n):
    if n>1:
        return a(n-1)+a(n+1)
    elif n==1:
        return 1
    else:
        return 0

def b1(n):
    if n>=1:
        return al**n+be**n
    else:
        return 0
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

plt.stem(k,RHS1_vec(k),markerfmt='go',linefmt='g')
plt.stem(k,LHS1_vec(k),markerfmt='ro',linefmt='r:')
plt.grid()
plt.savefig("./1.1.png")
plt.show()

def LHS2(k):
    sum=0
    for i in range(1,k+1):
        sum+=a(i)/10**i
    return sum

LHS2_vec=np.vectorize(LHS2)

l=np.arange(1,10)

plt.axhline(y=10/89,c='b')
plt.stem(l,LHS2_vec(l),linefmt='r-')
plt.grid()
plt.savefig("./1.2.png")
plt.show()

b_vec=np.vectorize(b)
b1_vec=np.vectorize(b1)
plt.stem(k,b_vec(k))
plt.stem(k,b1_vec(k),linefmt='r:')
plt.grid()
plt.savefig("./1.3.png")
plt.show()

def LHS4(k):
    sum=0
    for i in range(1,k+1):
        sum+=b(i)/10**i
    return sum

LHS4_vec=np.vectorize(LHS4)


plt.axhline(y=8/89,c='b')
plt.axhline(y=12/89,c='g')
plt.stem(l,LHS4_vec(l),linefmt='r-')
plt.grid()
plt.savefig("./1.4.png")
plt.show()
