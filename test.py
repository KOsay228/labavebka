import unittest

def add_numbers(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
