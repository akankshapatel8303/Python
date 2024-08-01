import sympy as smp

x, y = smp.symbols('x y')

print(x**2)
print(x**2+y)

f = x**2 + y
print(f.subs(x,4))

print(smp.sin(x))
print(smp.asin(x))
print(smp.sec(x))
