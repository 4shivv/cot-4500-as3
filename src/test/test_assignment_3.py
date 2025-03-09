import unittest
from src.main.assignment_3 import euler_method, runge_kutta_method, f

class TestAssignment3(unittest.TestCase):
    def test_euler_method(self):
        a = 0  # Start of range
        b = 2  # End of range
        n = 10  # Number of iterations
        initial_condition = 1  # f(0) = 1
        
        expected = 1.2446380979332121
        actual = euler_method(f, a, b, n, initial_condition)
        self.assertAlmostEqual(expected, actual, places=10)
    
    def test_runge_kutta_method(self):
        a = 0  # Start of range
        b = 2  # End of range
        n = 10  # Number of iterations
        initial_condition = 1  # f(0) = 1
        
        expected = 1.251316587879806
        actual = runge_kutta_method(f, a, b, n, initial_condition)
        self.assertAlmostEqual(expected, actual, places=10)

if __name__ == "__main__":
    unittest.main()