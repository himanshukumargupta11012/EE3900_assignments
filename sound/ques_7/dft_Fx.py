import numpy as np

N=6

F_N=np.empty([N,N],dtype=complex)

for i in range(N):
  for k in range(i+1):
    F_N[i][k]=np.exp(-1j*2*np.pi*i*k/N)
    if i!=k:
      F_N[k][i]=F_N[i][k]
print(F_N)

x=np.array([[1],[2],[3],[4],[2],[1]])

X=np.dot(F_N,x)

print(X)
