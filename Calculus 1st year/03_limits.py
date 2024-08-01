import sympy as smp
x = smp.symbols('x')

p = 2*smp.exp(1/x)/(smp.exp(1/x)+1)
q = smp.limit(2*smp.exp(1/x)/(smp.exp(1/x)+1), x, 0, dir='+')
print(p)
print(q)


r = smp.limit(2*smp.exp(1/x)/(smp.exp(1/x)+1), x, 0, dir='-')
print(r)

s = smp.limit(((smp.cos(x)-1)/x), x, smp.oo)
print(s)