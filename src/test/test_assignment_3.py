from src.main.assignment_3 import euler_method, runge_kutta_method

def test_methods():
    f = lambda t, y: t - y**2
    y0 = 1
    t0 = 0
    t_end = 2
    n = 10

    euler_result = euler_method(f, y0, t0, t_end, n)
    runge_kutta_result = runge_kutta_method(f, y0, t0, t_end, n)

    assert abs(euler_result - 1.2446380979332121) < 1e-6
    assert abs(runge_kutta_result - 1.251316588789806) < 1e-6
