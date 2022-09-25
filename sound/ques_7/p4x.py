import numpy as np

P_4=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])

print(P_4)

x=np.array([[1],[2],[3],[4],[2],[1]])

print(x)

# P_4_pad=np.pad(P_4,(0,2))



# npad = [(0, 0)] * P_4.ndim
# npad[axis] = (0, pad_size)

# np.pad(array, pad_width=npad, mode='constant', constant_values=0)

