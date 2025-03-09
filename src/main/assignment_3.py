import numpy as np

def euler_method(f, a, b, n, initial_condition):
    """
    Implements the Euler method for solving differential equations
    
    Parameters:
    f (function): The derivative function dy/dt = f(t, y)
    a (float): Start of the interval
    b (float): End of the interval
    n (int): Number of iterations
    initial_condition (float): The initial value y(a)
    
    Returns:
    float: The approximated solution at point b
    """
    h = (b - a) / n  # Step size
    t = a
    y = initial_condition
    
    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h
        
    return y

def runge_kutta_method(f, a, b, n, initial_condition):
    """
    Implements the 4th order Runge-Kutta method for solving differential equations
    
    Parameters:
    f (function): The derivative function dy/dt = f(t, y)
    a (float): Start of the interval
    b (float): End of the interval
    n (int): Number of iterations
    initial_condition (float): The initial value y(a)
    
    Returns:
    float: The approximated solution at point b
    """
    h = (b - a) / n  # Step size
    t = a
    y = initial_condition
    
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        t = t + h
        
    return y

def f(t, y):
    """
    The derivative function representing the differential equation dy/dt = t - y^2
    """
    return t - y**2

def main():
    # Problem parameters
    a = 0  # Start of range
    b = 2  # End of range
    n = 10  # Number of iterations
    initial_condition = 1  # f(0) = 1
    
    # Solving using Euler method
    euler_result = euler_method(f, a, b, n, initial_condition)
    print(f"{euler_result}")
    
    # Solving using Runge-Kutta method
    rk_result = runge_kutta_method(f, a, b, n, initial_condition)
    print(f"{rk_result}")

if __name__ == "__main__":
    main()