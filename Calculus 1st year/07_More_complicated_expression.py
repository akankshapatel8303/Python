import sympy as smp
x = smp.symbols('x')
p = smp.integrate((1 + smp.sqrt(x))**smp.Rational(1, 3)/smp.sqrt(x), x)
print(p)

q = smp.integrate((x*(1-x**2)**smp.Rational(1, 4)), x)
print(q)

r = smp.integrate(((2*x-1)*smp.cos(smp.sqrt(3*(2*x-1)**2 + 6)) / smp.sqrt(3*(2*x-1)**2 + 6)), x)
print(r)