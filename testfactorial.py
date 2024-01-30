from factorial import Factorial
import unittest


class TestFactorial(unittest.TestCase):

  def setUp(self):
    self.factor = Factorial(self)

  def test_factorial(self):
    self.assertEqual(self.factor.factorial(10), 3628800,
                     "Factorial of 10 is 3628800")
    self.assertEqual(self.factor.factorial(2), 2, "Factorial of 2 is 2")

if __name__ == "__main__":
  unittest.main()