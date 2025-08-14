# Import the necessary libraries from SymPy
from sympy import symbols, Function, dsolve, Eq, Derivative

# Define the symbolic variables
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
# For example, let's solve the equation: y'' + y = 0
ode = Eq(y.diff(x, x) + y, 0)

# Use dsolve to solve the differential equation
solution = dsolve(ode, y)

# Print the original differential equation and the solution
print("Original Differential Equation:")
print(ode)
print("\nSolution:")
print(solution)

# To run this script, make sure you have SymPy installed:
# pip install sympy
