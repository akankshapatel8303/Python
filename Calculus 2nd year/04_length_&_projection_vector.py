import numpy as np
import sympy as smp
from sympy.vector import *
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import quad_vec

x, y, z, u1, u2, u3, v1, v2, v3, t = smp.symbols('x y z u_1 u_2 u_3 v_1 v_2 v_3 t')

#Numerical and symbolic
a = np.array([1,2,3])
b = np.array([7,8,9])
u = smp.Matrix([u1,u2,u3])
v = smp.Matrix([v1,v2,v3])

#Length of vector
p = np.linalg.norm(a)
print(p)

q = u.norm()
print(q)

#Projection od vector
# projv(u) = (u.v/|v|**2)v
proj_b_a = np.dot(a, b)/np.linalg.norm(b)**2 *b
print(proj_b_a)

proj_v_u = u.dot(v)/v.norm()**2 * v
print(proj_v_u)