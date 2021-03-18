from sympy import *

init_printing()
x = Symbol('x')
f = 1 / (x + 1) / sqrt(x + 1)
print(integrate(f, (x, 1, +oo)))

# сходится
