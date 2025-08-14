coursera-rprog-06-ProgrammingAssignment2
========================================

Coursear R Programming

## Solving Ordinary Differential Equations with Python and SymPy

This repository contains a Python script, `ode_solver.py`, that demonstrates how to solve ordinary differential equations (ODEs) using the SymPy library.

### Overview of Solving ODEs with SymPy

SymPy is a Python library for symbolic mathematics. It provides a powerful function called `dsolve` that can be used to solve a wide variety of ordinary differential equations. The process generally involves:

1.  **Defining Symbolic Variables**: Using `sympy.symbols` to declare the independent and dependent variables.
2.  **Defining the Function**: Defining the dependent variable as a function of the independent variable using `sympy.Function`.
3.  **Creating the Differential Equation**: Expressing the ODE as an equation using `sympy.Eq`. Derivatives are represented using the `.diff()` method.
4.  **Solving the Equation**: Using `sympy.dsolve` to find the general solution to the ODE.

### How to Run the Script

1.  **Install SymPy**:
    If you don't have SymPy installed, you can install it using pip:
    ```bash
    pip install sympy
    ```

2.  **Run the script**:
    Execute the `ode_solver.py` script from your terminal:
    ```bash
    python ode_solver.py
    ```

The script will print the original differential equation and its solution to the console.

