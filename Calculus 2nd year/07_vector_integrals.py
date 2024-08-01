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

#vector integrals
#Note: Will not add the +C
r = smp.Matrix([smp.exp(t)*smp.cos(t), t**4, 1/(t**2 + 1)])
print(r)
print(smp.integrate(r, t))

#In the cases integral cannot be evaluated symbolically: must solve definite integrals numerically.
p = smp.Matrix([smp.exp(t**2)*smp.cos(t)**3, smp.exp(-t**4), 1/(t**2+3)])
print(p)

#Integrate from t=0 to 4
r_num = smp.lambdify([t], r)
print(quad_vec(r_num, 0, 4)[0])