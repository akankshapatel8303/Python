import sympy as smp

x = smp.symbols('x')
p = smp.integrate((16*smp.atan(x)/(1+x**2)), (x, 0, smp.oo))
print(p)