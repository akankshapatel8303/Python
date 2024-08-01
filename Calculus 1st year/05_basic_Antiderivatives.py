import sympy as smp

x = smp.symbols('x')

p = smp.integrate(smp.csc(x) * smp.cot(x) , x)
print(p)

q = smp.integrate((4 * smp.sec(3*x) * smp.tan(3*x)), x)
print(q)

r = smp.integrate((2/smp.sqrt(1-x**2) - 1/x**smp.Rational(1,4)), x)
print(r)

