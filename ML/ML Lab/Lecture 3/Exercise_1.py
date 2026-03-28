import numpy as np
## -- Problem 8
# X = np.random.rand(5,5)
# col_sums = np.sum(X, axis=0)
# max_col_index = np.argmax(col_sums) # 가장 큰 값이 있는 위치(index) 찾기

# first_three = np.sum(X[:,:3], axis=1)
# last_two = np.sum(X[:, -2:], axis=1)
# condition = first_three > last_two
# indices = np.where(condition) 
# print(indices)


## -- Problem 7
# top = np.eye(10)[1::2][::-1]
# bottom = np.flipud(top)
# matrix = np.vstack([top, bottom])
# print(matrix)

## -- Problem 6
# X = np.ones((10,10))
# X[2:8, 2:8] = 0
# Y = np.full((10,10), -1)
# A = np.arange(40).reshape(5,5)
# Y[1:6,1:6] = A

## -- Problem 5 
# Base = np.ones((11,11))
# A = np.abs(np.arange(-5, 6))
# Base[np.diag_indices_from(Base)] = A
# print(Base)

## -- Problem 4 : 1. create a 2D numpy array  𝐴  such that  𝐴𝑖𝑗=𝑖×𝑗,
## but without using list comprehensions. Use broadcasting instead
## 2. Use array broadcasting to create a (10,10) numpy array with values
# A = np.arange(1,10).reshape(-1,1) # Shape: (5, 1)
# B = np.arange(1,10).reshape(1,-1) # Shape: (1, 5)

# result = A * B
# print(result)

## -- Problem 1 : Create a numpy array that contain intergers i 
## -- such that 0<i<100 and  2^𝑖  has the last digit 6
# arr = np.array([2**i for i in range(6)])

## -- Problem 2 : Create a 2D numpy array  𝐴  such that  𝐴𝑖𝑗=𝑖×𝑗
# arr_2d = arr.reshape(2)

## -- Problem 3 : Create an array of first 10 powers of 2
# powers_of_2 = 2 ** np.arange(10)
# print(powers_of_2)

