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

#vector derivatives
r = smp.Matrix([3*t, smp.sin(t), t**2])
q = smp.diff(r, t)
print(q)

# Q1- find the angle between the velocity and acceleration as a function of time 0(t)
v = smp.diff(r, t)
a = smp.diff(v, t)
theta = smp.acos(v.dot(a)/(v.norm()*a.norm()))
print(theta)

print(theta.subs(t, smp.pi))
print(theta.subs(t, smp.pi).evalf())

#Graph
tt = np.linspace(0, 10, 100)
aa = smp.lambdify([t], theta)(tt)
plt.plot(tt, aa)
plt.xlabel('$t$', fontsize = 20)
plt.xlabel(r'$\theta(t)$', fontsize = 20)
print(plt.show())