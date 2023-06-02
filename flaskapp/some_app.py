import unittest

def summa(a, b):
return a * b

class TestAddition(unittest.TestCase):
def test_addition(self):
result = summa(2, 3)
self.assertEqual(result, -1)

if __name__ == '__main__':
unittest.main()
