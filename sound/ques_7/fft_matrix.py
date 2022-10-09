from array import array
import numpy as np



def F_n(n,F_n):
  if(n==1):
    return [[1]]
  else:
    # print(np.matmul(D_n(n),F_n))
    a=np.matmul(np.bmat([[F_n,np.matmul(D_n(n),F_n)],[F_n,-np.matmul(D_n(n),F_n)]]),P_n(n))
    # print(a)
    return a

def P_n(n):
  arr=np.zeros((n,n),dtype=int)
  for i in range(n):
    if i<n/2:
      arr[2*i][i]=1
    else:
      arr[2*(i-int(n/2))+1][i]=1
  return arr

def D_n(n):
  W=np.exp(-1j*2*np.pi/n)
  list=[W**i for i in range(int(n/2))]
  return np.diag(list)

F_2=[[1]]
N=8

for i in range(int(np.log2(N))):
  F_2=F_n(2**(i+1),F_2)


x=np.array([1,2,3,4,2,1,0,0])

a=np.matmul(F_2,P_n(8))
# print(a)
print(np.matmul(a,x.T))
