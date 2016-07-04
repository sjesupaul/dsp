# Matrix Algebra

PLACE YOUR CODE HERE

import numpy
from numpy import matrix

# Matrices
a = matrix([[1, 2, 3], [2, 7, 4]])
b = matrix([[1, -1], [0, 1]])
c = matrix([[5, -1], [9, 1], [6,0]])
d = matrix([[3, -2, -1], [1, 2, 3]])
# Vectors
u = numpy.array([[6, 2, -3, 5]])
v = numpy.array([[3, 5, -1, 4]])
w = numpy.array([[1], [8], [0], [5]])


# 1. Matrix Dimensions
print('#1. Matrix Dimensions\n')
print('1.1) Dimensions of Matrix A:', a.shape) # Answer: 2x3
print('1.2) Dimensions of Matrix B:', b.shape) # Answer: 2x2
print('1.3) Dimensions of Matrix C:', c.shape) # Answer: 3x2
print('1.4) Dimensions of Matrix D:', d.shape) # Answer: 2x3
print('1.5) Dimensions of Vector u:', u.shape) # Answer: 1x4
print('1.6) Dimensions of Vector w:', w.shape) # Answer: 4x1


# 2. Vector Operations
print('\n#2. Vector Operations\n')
print('2.1) u+v =', u+v) # Answer: [9 7 -4 9]
print('2.2) u-v =', u-v) # Answer: [3 -3 -2 1]
print('2.3) 6u =', 6*u) # Answer: [36 12 -18 30]
print('2.4) uv =', numpy.dot(u, v)) # Answer: 51
print('2.5) ||u|| =', numpy.linalg.norm(u)) # Answer: sqrt(74) ≈ 8.60232526704


# 3. Matrix Operations

print('\n#3. Matrix Operations\n')

try:
    print ('3.1) A + C = \n', a+c)
except:
    print('3.1) A + C = Not defined, due to dimension mismatch')

try:
    print('3.2) A + C^T = \n', a+c.transpose())
except:
    print('3.2) A + C^T = Not defined, due to dimension mismatch')

try:
    print('3.3) C^T + 3D= \n', c.transpose()+(3*d))
except:
    print('3.3) C^T + 3D = Not defined, due to dimension mismatch')

try:
    print('3.4) BA = \n', numpy.dot(b, a))
except:
    print('3.4) BA = Not defined, because the number of columns in B != to the number of rows in A')

try:
    print('3.5) B + A^T = \n', numpy.dot(b, a.transpose()))
except:
    print('3.5) B + A^T = Not defined, because the number of columns in B != to the number of rows in A^T')

try:
    print('3.6) BC = \n', numpy.dot(b, c))
except:
    print('3.6) BC = Not defined, because the number of columns in B != to the number of rows in C')

try:
    print('3.7) CB = \n', numpy.dot(c, b))
except:
    print('3.7) CB = Not defined, because the number of columns in C != to the number of rows in B')

print('3.8) B^4 = \n', numpy.linalg.matrix_power(b, 4))

try:
    print('3.9) A(A^T) = \n', a*a.transpose())
except:
    print('3.9) A(A^T) = Not defined, because the number of columns in A != to the number of rows in A^T')

try:
    print('3.10) (D^T)D = \n', d.transpose()*d)
except:
    print('3.10) (D^T)D = Not defined, because the number of columns in D^T != to the number of rows in D')

# Answers for #3:
# 3.1) Not defined, due to dimension mismatch
# 3.2) [[6 11 9][1 8 4]]
# 3.3) [[14 3 3][2 7 9]]
# 3.4) [[-1 -5 -1][2 7 4]]
# 3.5) Not defined, since number of columns in B != number of rows in A^T
# 3.6) Not defined, since number of columns in B != number of rows in C
# 3.7) [[5 -6][9 -8][6 -6]]
# 3.8) [[1 -4][0 1]]
# 3.9) [[14 28][28 69]]
# 3.10) [[10 -4 0][-4 8 8][0 8 10]]
