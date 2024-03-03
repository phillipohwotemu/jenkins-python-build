# Example test_ops.py
import unittest
from ops import add  # Assume this is a function you want to test

class TestOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
