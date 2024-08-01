import sympy as smp

n = smp.symbols('n')
p = smp.Sum(6/4**n, (n, 0, smp.oo)).doit()
print(p)

q = smp.Sum((2**(n+1)/5**n), (n, 0, smp.oo)).doit()
print(q)

r = smp.Sum((smp.atan(n)/n**smp.Rational(11,10)), (n, 1, smp.oo)).n()
print(r)

s = smp.Sum((1+smp.cos(n))/n, (n, 1, smp.oo)).n()
print(s)

t = smp.Sum((1+smp.cos(n))/n**2, (n, 1, smp.oo)).n()
print(t)