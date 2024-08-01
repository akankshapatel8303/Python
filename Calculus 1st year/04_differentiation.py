import sympy as smp
x = smp.symbols('x')

p = smp.diff(((1+smp.sin(x))/(1-smp.cos(x)))**2, x)
print(p)

q = smp.diff((smp.log(x, 5))**(x/2), x)
print(q)

f, g = smp.symbols('f g', cls=smp.Function)
g = g(x)
f = smp.diff(f(x+g), x)
print(f)