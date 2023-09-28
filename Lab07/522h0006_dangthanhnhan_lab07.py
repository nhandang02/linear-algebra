# -*- coding: utf-8 -*-
"""522h0006_DangThanhNhan_Lab7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f1vApKpT9CaYNxvniCG-bWAM86IQEXtO

**Đặng Thành Nhân-MSSV:522H0006-Nhóm 8 tổ 2 -Lab7**
"""

# Exercise 1
import numpy as np

def checkLinear(maxtrix1 , maxtrix2):
  if a==b:
    print("W is linear combination of v1, v2, v3")
  else:
    print("W is not linear combination of v1, v2, v3")

#a
print("a)")
v1 = np.array([1, 2, 3, 4])
v2 = np.array([-1, 0, 1, 3])
v3 = np.array([0, 5, -6, 8])
w = np.array([3, -6, 17, 11])

A = np.column_stack([v1, v2, v3])
Aw = np.column_stack((A, w))
print("A =", A, sep="\n")
print()
print("Aw =", Aw, sep="\n")

a = np.linalg.matrix_rank(A)
b = np.linalg.matrix_rank(Aw)

checkLinear(a, b)
print()

#b
print("b)")
v1 = np.array([1, 1, 2, 2])
v2 = np.array([2, 3, 5, 6])
v3 = np.array([2, -1, 3, 6])
w = np.array([0, 5, 3, 0])

A = np.column_stack([v1, v2, v3])
Aw = np.column_stack((A, w))
print("A =", A, sep="\n")
print()
print("Aw =", Aw, sep="\n")

a = np.linalg.matrix_rank(A)
b = np.linalg.matrix_rank(Aw)
checkLinear(a, b)
print()

#c
print("c)")
v1 = np.array([1, 1, 2, 2])
v2 = np.array([2, 3, 5, 6])
v3 = np.array([2, -1, 3, 6])
w = np.array([-1, 6, 1, -4])

A = np.column_stack([v1, v2, v3])
Aw = np.column_stack((A, w))
print("A =", A, sep="\n")
print()
print("Aw =", Aw, sep="\n")

a = np.linalg.matrix_rank(A)
b = np.linalg.matrix_rank(Aw)
checkLinear(a, b)
print()

#d
print("d)")
v1 = np.array([1, 2, 3, 4])
v2 = np.array([-1, 0, 1, 3])
v3 = np.array([0, 5, -6, 8])
v4 = np.array([1, 15, -12, 8])
w = np.array([3, -6, 17, 11])

A = np.column_stack([v1, v2, v3, v4])
Aw = np.column_stack((A, w))
print("A =", A, sep="\n")
print()
print("Aw =", Aw, sep="\n")

a = np.linalg.matrix_rank(A)
b = np.linalg.matrix_rank(Aw)

checkLinear(a, b)

# Exercise 2
import numpy as np

# def checkInd(maxtrix):
#   det_A = np.linalg.det(A)
#   if det_A == 0:
#     print("Ma trận A không độc lập tuyến tính")
#   else:
#     print("Ma trận A độc lập tuyến tính")

def checkInd(maxtrix):
  rank_A = np.linalg.matrix_rank(A)
  n_rows = A.shape[0]

  if rank_A == n_rows:
    print("Ma trận độc lập tuyến tính.")
  else:
    print("Ma trận không độc lập tuyến tính.")
# a
print("a)")
v1 = (np.array([1, -2, 0])).T
v2 = (np.array([0, -4, 1])).T
v3 = (np.array([1, -1, 1])).T

A = np.column_stack([v1, v2, v3])

checkInd(A)
print()

# b
print("b)")
v1 = (np.array([1, 0, 2])).T
v2 = (np.array([0, 1, 4])).T
v3 = (np.array([2, -2, -4])).T

A = np.column_stack([v1, v2, v3])

checkInd(A)
print()

# c
print("c)")
v1 = (np.array([1, -2, 3, 4])).T
v2 = (np.array([2, 4, 5, 0])).T
v3 = (np.array([-2, 0, 0, 4])).T
v4 = (np.array([3, 2, 1, -1])).T

A = np.column_stack([v1, v2, v3, v4])

checkInd(A)
print()

# d
print("d)")
v1 = (np.array([0, 0, 1, 2, 3])).T
v2 = (np.array([0, 0, 2, 3, 1])).T
v3 = (np.array([1, 2, 3, 4, 5])).T
v4 = (np.array([2, 1, 0, 0, 0])).T
v5 = (np.array([-1, -3, -5, 0, 0])).T

A = np.column_stack([v1, v2, v3, v4, v5])

checkInd(A)

# Exercise 3
import numpy as np
import sympy as sp

C = np.array([[1, 0, 2, 3], [4, -1, 0, 2], [0, -1, -8, -10]])

#a
res = sp.Matrix(C).rref()
print("sp.Matrix(C).rref() =", res)
basisC = C[:, list(res[1])]
print("A basis for the colum space of C = \n", basisC)
print("We can create the third colum of C by the basis", 2*basisC[:, 0] + 8*basisC[:, 1])
print()

#b
C_T = np.transpose(C)
res = sp.Matrix(C_T).rref()
print("sp.Matrix(C).rref() =", res)
basisC_T = C.T[:, list(res[1])]
print("A basis for the colum space of C_T = \n", basisC_T)
print("We can create the third colum of C by the basis", 2*basisC_T[:, 0] + 8*basisC_T[:, 1])

# Exercise 4
import numpy as np

# Define A2 matrix
A2 = np.array([[1, 0, 2, 3], [4, -1, 0, 2], [0, -1, -8, -10]])

# Find basis for null-space of A2 using null_space function
null_space_basis = np.linalg.null_space(A2)

# Print basis vectors as columns
print("Basis for null-space of A2:")
if null_space_basis.size == 0:
    print("The matrix A2 has no non-trivial null-space.")
else:
    for i in range(null_space_basis.shape[1]):
        print(null_space_basis[:, i])

# Check if linear combination of basis vectors is in null-space
a = 2
b = 1
lc = a*null_space_basis[:, 0] + b*null_space_basis[:, 1]  # Note the "+" sign here
print("Linear combination:", lc)
if null_space_basis.size == 0 or np.allclose(A2.dot(lc), np.zeros(A2.shape[0])):
    print("Linear combination is in null-space")
else:
    print("Linear combination is not in null-space")

# Exercise 5
import numpy as np

# a
w = np.array([[1], [1], [-1], [-3]])
A = np.array([[7, 6, -4, 1], [-5, -1, 0, -2], [9, -11, 7, -3], [19, -9, 7, 1]])

col_space = np.linalg.matrix_rank(A)
null_space = A.shape[1] - col_space

if np.linalg.matrix_rank(np.concatenate((A, w), axis=1)) == col_space:
    print("w is in the column space of A.")
elif np.linalg.matrix_rank(np.concatenate((A, w), axis=1)) == null_space:
    print("w is in the null space of A.")
elif np.linalg.matrix_rank(np.concatenate((A, w), axis=1)) == col_space + null_space:
    print("w is in both the column space and null space of A.")
else:
    print("w is not in the column space or null space of A.")

# b
import numpy as np

w = np.array([[1], [2], [1], [0]])
A = np.array([[-8, 5, -2, 0], [-5, 2, 1, -2], [10, -8, 6, -3], [3, -2, 1, 0]])

col_space = np.linalg.matrix_rank(A)
null_space = A.shape[1] - col_space

if np.linalg.matrix_rank(np.concatenate((A, w), axis=1)) == col_space:
    print("w is in the column space of A.")
elif np.linalg.matrix_rank(np.concatenate((A, w), axis=1)) == null_space:
    print("w is in the null space of A.")
elif np.linalg.matrix_rank(np.concatenate((A, w), axis=1)) == col_space + null_space:
    print("w is in both the column space and null space of A.")
else:
    print("w is not in the column space or null space of A.")

# Exercise 6
import numpy as np

# Define the matrix A
A = np.array([[5, 1, 2, 2, 0],
              [3, 3, 2, -1, -12],
              [8, 4, 4, -5, 12],
              [2, 1, 1, 0, -2]])

a1 = A[:, 0]
a2 = A[:, 1]
a4 = A[:, 3]

# Define the matrix B
B = np.column_stack((a1, a2, a4))

a3 = A[:, 2]
a5 = A[:, 4]

if np.allclose(a3, 2 * a1 + 2 * a2 - 5 * a4):
    print("a3 is in the column space of B")
else:
    print("a3 is not in the column space of B")

if np.allclose(a5, 12 * a1 - 12 * a2 + 12 * a4):
    print("a5 is in the column space of B")
else:
    print("a5 is not in the column space of B")

# Exercise 7
import numpy as np

A = np.array([[1, 0, 2], [0, 1, 4], [2, -2, -4]])

dim_span = np.linalg.matrix_rank(A)

rref, _ = np.linalg.qr(A)
basis = rref[:, :dim_span]

print("Dimension of span:", dim_span)
print("Basis for span:")
print(basis)

# Exercise 8
import numpy as np

# Create the Hilbert matrix A with size 5
A = np.array([[1/(i+j-1) for j in range(1,6)] for i in range(1,6)])
print("Hilbert Matrix")
print(A)

# Create matrix B
B = np.zeros((5,5))
for i in range(5):
    for j in range(i+1):
        if j == 0 or j == i:
            B[i][j] = 1
        else:
            B[i][j] = B[i-1][j-1] + B[i-1][j]
print("Pascal Matrix")
print(B)

# Create magic matrix C
n = 5
C = [[0 for x in range(n)] for y in range(n)]

i = n // 2
j = n - 1

num = 1
while num <= (n * n):
    if i == -1 and j == n:
        j = n - 2
        i = 0
    else:
        if j == n:
            j = 0
        if i < 0:
            i = n - 1
    if C[i][j]:
        j -= 2
        i += 1
        continue
    else:
        C[i][j] = num
        num += 1
    j += 1
    i -= 1
arr = np.array(C).flatten()
# Reshape mảng về dạng ma trận vuông
n = int(np.sqrt(len(arr)))
C_square = arr.reshape(n, n)
print("Magic matrix")
print(C_square)

# Find a basis for the null space of Hilbert Matrix
u, s, vh = np.linalg.svd(A)
null_space_basis_A = vh[np.sum(s > 1e-10):,:].T

# Find a basis for the null space of Pascal Matrix
u, s, vh = np.linalg.svd(B)
null_space_basis_B = vh[np.sum(s > 1e-10):,:].T

# Find a basis for the null space of Magic Matrix
u, s, vh = np.linalg.svd(C_square)
null_space_basis_C = vh[np.sum(s > 1e-10):,:].T

print("Basis for the null space of Hilbert Matrix:")
print(null_space_basis_A)

print("Basis for the null space of Pascal Matrix:")
print(null_space_basis_B)

print("Basis for the null space of Magic Matrix:")
print(null_space_basis_C)

# Exercise 9
import numpy as np

def is_orthogonal_set(vectors):
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            if vectors[i].shape != vectors[j].shape:
                return False
            if np.dot(vectors[i], vectors[j]) != 0:
                return False
    return True

u1 = np.array([3, 1, 1])
u2 = np.array([-1, 2, 1])
u3 = np.array([-1/2, 2, 7, 2])

vectors = [u1.T, u2.T, u3.T]

if is_orthogonal_set(vectors):
    print("The vectors are orthogonal.")
else:
    print("The vectors are not orthogonal.")

# Exercise 10
import numpy as np

def orthogonal_projection(y, u):
    projection = np.dot(y, u) / np.dot(u, u) * u
    return projection

y = np.array([7, 6])
u = np.array([4, 2])

proj_u_y = orthogonal_projection(y.T, u.T)
print("The orthogonal projection of y onto u is:", proj_u_y)

# Exercise 11
import numpy as np

def is_orthonormal_columns(A):
    m, n = A.shape

    for j in range(n):
        if not np.isclose(np.linalg.norm(A[:,j]), 1):
            return False

    for j in range(n):
        for k in range(j+1, n):
            if not np.isclose(np.dot(A[:,j], A[:,k]), 0):
                return False

    return True

# Exercise 12
import numpy as np

A = np.array([[-10, 13, 7, -11],
              [2, 1, -5, 3],
              [-6, 3, 13, -3],
              [16, -16, -2, 5],
              [2, 1, -5, -7]])

Q, R = np.linalg.qr(A)
ortho_basis = Q[:,:np.linalg.matrix_rank(A)]
print("Orthonormal basis for column space of A:")
print(ortho_basis)