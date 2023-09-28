# -*- coding: utf-8 -*-
"""522H0006_DangThanhNhan_Lab05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19C47B7PgMpl4XtSri0OF8t9-pWPcyqyA

**Đặng Thành Nhân-MSSV:522H0006-Nhóm 8 tổ 2 -Lab5**
"""

#Exercise 15:
import numpy as np
A15 = []
A = np.random.randint(1, 100, (10 ,10))
print(A)
for i in range(10):
  if i % 2 == 1:
    A15 = A15 + [np.flipud(A[i, :])]
  else:
    A15 = A15 + [A[i,:]]
A15 = np.reshape(A15,(10, 10))
print(A15)

#Exercise 16:
import numpy as np
m = 10
n = 10
A = np.random.randint(1, 100, (m ,n))
print(A)
max = 0
for i in range(3):
  for j in range(3):
    if(A[i,j] > max and A[i,j] % 2 == 1):
      max = A[i,j]
print(max)

for i in range(10):
  for j in range(10):
    if (A[i,j] % 2 == 1):
      A[i,j] = max

print(A)

#Exersice 17:
import numpy as np
m = 10
n = 10
A = np.random.randint(1, 100, (m ,n))
print(A)
print()
t = 0
for i in range(10):
  t = A[i,j]
  A[i, 0] = A[i,0]
  A[i,0] = t
print(A)

#Exercise 18:
import numpy as np
m = 10
n = 10
A = np.random.randint(1, 100, (m ,n))
print(A)
S = 0
for i in range(10):
  for j in range(10):
    S = S + A[i,j]
print("S = ", S)

#Exercise 19:
import numpy as np
m = 10
n = 10
A = np.random.randint(1, 100, (m ,n))
print(A)
A19 = np.diag(A, 0)
print(A19)

#Exercise 20:
import numpy as np
import sympy as sp
x, c1, c2, c3, c4 = sp.symbols('x, c1, c2, c3, c4')
pt = lambda x: c1 + c2*x + c3*x**2 + c4*x**3
print(pt(1))
print(pt(2))
print(pt(3))
print(pt(4))
pt1 = sp.Eq(pt(1), 1000)
pt2 = sp.Eq(pt(2), 2000)
pt3 = sp.Eq(pt(3), 3000)
pt4 = sp.Eq(pt(4), 4000)
sol = sp.solve((pt1, pt2, pt3, pt4), (c1, c2, c3, c4))
print("solution =", sol)