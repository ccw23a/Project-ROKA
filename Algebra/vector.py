import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
##          [1, 2, 3]
##  x   =   [4, 5, 6]   

print("\n")

y = np.array([[5, 6, 7], [7, 8, 9]])
print(y)
##  y   =   [5, 6, 7]
##          [7, 8, 9]

print("\n")


print(np.array_equal(x, y))
##행렬이 같지 않으므로 False


