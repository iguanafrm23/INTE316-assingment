import sympy as sp # type: ignore

# Define the variable and function
x = sp.symbols('x')
f = x**2 + 3*x + 2

# Differentiate the function
f_prime = sp.diff(f, x)
f_prime
