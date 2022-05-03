import numpy as np

a = np.arange(15).reshape(3,5)
b = np.array([[ 0, 1, 2, 3, 4],[ 5, 6, 7, 8, 9],[10, 11, 12, 13, 14]])
print(a,type(a))
print(b,type(a))
print("shape of a: ",a.shape)
print("dimention of a: ",a.ndim)
print("size of a: ",a.size)

