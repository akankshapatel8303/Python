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

#lines
#vector r(t) = vector r0 + t*v
r0 = smp.Matrix([1,1,1])
v = smp.Matrix([1,3,-1])
r = r0 + t*v
print(r)

#plane
#vec n.(P0 - r) = 0
n = smp.Matrix([1,1,1])
P0 = smp.Matrix([3,4,6])
r = smp.Matrix([x,y,z])
sol =n.dot(P0 - r)
print(sol)

# Q1- Find vector parallel to the line of intersection of the two planes 3x-6y-2z = 15 and 2x+y-2z=5. (Its going to be perpendicular to both normal vectors)
n1 = np.array([-3,6,2])
n2 = np.array([-2,-1,2])
ans = np.cross(n1, n2)
print(ans)

