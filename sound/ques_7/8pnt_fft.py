import numpy as np
import time
import matplotlib.pyplot as plt

def W(N,k):
  return np.exp(-1j*2*np.pi*k/N)

def FFT(N,k,x):

  if N%2==0:
    x1=[]
    x2=[]
    for i in range(int(N)):
      if i%2==0:
        x1.append(x[i])
      else:
        x2.append(x[i])
    return FFT(N/2,k,x1)+W(N,k)*FFT(N/2,k,x2)
  
  elif N==1:
    return x[0]
  
  else:
    print("can't find FFT")

x=[1,2,3,4,2,1,0,0]
for i in range(1500):
  x.append(0)
  
N=8
X=[]
times_FFT=10
time_FFT=[]
for j in range(times_FFT):
  ini_time=time.process_time()
  # X.append([])
  for i in range(2**j):
    x.append
    # X[j].append(FFT(N,i,x))
    m=FFT(2**j,i,x)
  time_FFT.append(time.process_time()-ini_time)
# print(X)
print(time_FFT)



times_DFT=600
time_DFT=[]

def x(n):
    if n<0 or n>5:
        return 0
    elif n<4:
     return n+1
    else:
        return 6-n
def dft(k):
    l=0
    for i in range(N):
        l+=x(i)*np.exp(-1j*2*np.pi*k*i/N)
    return l



v=[2**i for i in range(times_FFT)]


for i in range(times_DFT):
  ini_time=time.process_time()
  dft2=np.vectorize(dft)
  A=dft2(range(i+1))
  time_DFT.append(time.process_time()-ini_time)
  # for j in range(i):







plt.plot(v,time_FFT)
plt.plot(range(times_DFT),time_DFT)
plt.xlim(0,600)
plt.grid()
plt.legend(['fft','dft'])
plt.show()
