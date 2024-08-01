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

#Arclength
# L = integration limit from a to b sqrt(dx**2 + dy**2 + dz**2) = integration limit from a to b sqrt((dx/dt)**2 + (dy/dt)**2 + (dz/dt)**2)dt

#Rare cases can be done symbolically. Find arclength of (0, t, t**2) from t = 0 to 1
r = smp.Matrix([0, t, t**2])
p = smp.integrate(smp.diff(r, t).norm(), (t,0,1))
print(p)

#In most cases need to be done numerically. Find the arclength of (e**t, sint, t**4) from t=0 to t=1
q = smp.Matrix([smp.exp(t), smp.sin(t), t**4])
q_num = smp.lambdify([t], smp.diff(q,t).norm())
print(quad(q_num, 0, 1)[0])
