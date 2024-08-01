import sympy as smp

x = smp.symbols('x')

ques = smp.sin(x/2 + smp.sin(x))
sol = smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi)

print(ques)
print(sol)

p = smp.log(x, 10)
print(p)

q = x**(3/2)
print(q)

r = x**(smp.Rational(3, 2))
print(r)