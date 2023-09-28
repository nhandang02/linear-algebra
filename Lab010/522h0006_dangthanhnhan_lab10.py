# -*- coding: utf-8 -*-
"""522H0006_DangThanhNhan_Lab10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10yTZF44zGFnW6Bhcu9b8LlqYaDCWR_CP

**Đặng Thành Nhân-MSSV:522H0006-Nhóm 8 tổ 2 -Lab10**
"""

# Exercise 1
import numpy as np
A = np.array([[-1, 3.5, 14],
              [0, 5, -26],
              [0, 0, 2]])
B = np.array([[-2, 0, 0],
              [99, 0, 0],
              [10, -4.5, 10]])
C = np.array([[5, 5, 0, 2],
              [0, 2, -3, 6],
              [0, 0, 3, -2],
              [0, 0, 0, 5]])
D = np.array([[3, 0, 0, 0],
              [6, 2, 0, 0],
              [0, 3, 6, 0],
              [2, 3, 3, -5]])
E = np.array([[3, 0, 0, 0, 0],
              [-5, 1, 0, 0, 0],
              [3, 8, 0, 0, 0],
              [0, -7, 2, 1, 0],
              [-4, 1, 9, -2, 3]])
def Eigenvalues(matrix):
  eval = np.linalg.eigvals (matrix)
  print("1. eigenvalues = ", eval) #eigenvalues
  w, v = np.linalg.eig(matrix)
  print("2. eigenvalues = ", w) #eigenvalues =
  print("3. eigenvectors = ", v) #columns of the matrix v are eigenvectors
  print()

Eigenvalues(A)
Eigenvalues(B)
Eigenvalues(C)
Eigenvalues(D)
Eigenvalues(E)

#Exercise 2:
import numpy as np
a12 = [32, 31.9, 31.8, 32.1, 32.2]
for a in a12:
  E2a = np.array([[-6, 28, 21],
                  [4, -15, -12],
                  [8,a,25]])

  #w, v np.linalg.eig(E2a)
  w = np.linalg.eigvals (E2a)
  print("Eigenvalues with a = ",a, "is: ", w)
  E2a = np.array([[-6, 28, 21], [4, -15, -12], [8,a,25]])
  print("Eigenvalues of A with a = ",a, "is: ", w) # trị riêng

#Plot đồ thị
from matplotlib import pyplot as plt
from sympy import *
A = np.array([[-6, 28, 21],[4, -15, -12],[8, 0, 15]])
#alpha = np.array([32, 31.9, 31.8, 32.1, 32.2])
alpha = [32, 31.9, 31.8, 32.1, 32.2]
color = ['b', 'r', 'g', 'k', 'c', 'm']
t = symbols('t')
x = np.arange(0, 3, 0.05)
fig = plt.figure()
#for i, alp in enumerate(alpha):  #alpha = [32, 31.9, 31.8, 32.1, 32.2]
i = 0
for alp in alpha:  #alpha = [32, 31.9, 31.8, 32.1, 32.2]
    B = A  #Sao chép ma trận A sang ma trận B
    B[2,1] = alp # Gán tham số a vào ma trận B
    lambd = np.linalg.eigvals(B)
    p = 1

    for j in range(len(lambd)):
      p = p*(lambd[j] - t)
    y = lambdify(t, p, "numpy")(x)
    plt.plot(x, y, color[i])
    i = i + 1
plt.show()

#Exercise 5:
import numpy as np
#An n×n-matrix A is said to be diagonalizable if it can be written on the form
#  A = P * D * P^-1
#where D is a diagonal n×n matrix with the eigenvalues of A,
#and P is a nonsingular n×n matrix consisting of the eigenvectors
import numpy as np

def checkDiagonalizable(A):
  w, P = np.linalg.eig(A) # w is eigenvalues of A; P is vectorvalues of A
  print("w = ",w)
  D = np.diag(w) #Chuyển thành ma trận đường chéo của w
  print("D = \n",D)
  print("--------")
  P_1 = np.linalg.inv(P)

  res = np.matmul(np.matmul(P,D),P_1)
  print("res = \n",res)
  return np.allclose(A, res) #if A = res return True

A1 = np.array([[4, -5],
               [2, -3]])
print(checkDiagonalizable(A1))

A2 = np.array([[0, 2],
               [0, 1]])
print(checkDiagonalizable(A2))

A3 = np.array([[2, 3],
               [1, 4]])
print(checkDiagonalizable(A3))

A4 = np.array([[1, 2, -2],
               [-2, 5, -2],
               [-6, 6, -3]])
print(checkDiagonalizable(A4))

A5 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])
print(checkDiagonalizable(A5))