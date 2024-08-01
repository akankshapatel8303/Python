import sympy as smp

x = smp.symbols('x')
integral = smp.integrate((8*x + smp.csc(x)**2), x)
print(integral)

c = -integral.subs(x, smp.pi/2) - 7
print(c)

final = integral + c
print(final)