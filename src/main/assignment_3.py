
import numpy as np

def euler_method(f, y0, t0, t_end, n):
    h = (t_end - t0) / n
    t = t0
    y = y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

def runge_kutta_method(f, y0, t0, t_end, n):
    h = (t_end - t0) / n
    t = t0
    y = y0
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return y

if __name__ == "__main__":
    f = lambda t, y: t - y**2
    y0 = 1
    t0 = 0
    t_end = 2
    n = 10

    euler_result = euler_method(f, y0, t0, t_end, n)
    runge_kutta_result = runge_kutta_method(f, y0, t0, t_end, n)

    print(euler_result)
    print(runge_kutta_result)
