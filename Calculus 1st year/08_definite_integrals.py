import sympy as smp

x, t = smp.symbols('x t')
p = smp.integrate((smp.exp(x)/smp.sqrt(smp.exp(2*x)+9)), (x, 0, smp.log(4)))
print(p)

q = smp.integrate((x**10 * smp.exp(x)), (x, 1, t))
print(q)